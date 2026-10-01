"""
Multilingual E5 embeddings via the delosis-embedding-api service.

The stock Harmony API loads its Hugging Face models in-process with
sentence-transformers. E5 is instead served by the delosis-embedding-api
container (intfloat/multilingual-e5-base, 768-d) that already backs Harmony
Discovery, so the API container gains a model without another ~1 GB of
weights or RAM. Same host, dedicated docker network (embedder-harmony).

E5 is an asymmetric model that expects a role prefix on every text. Item to
item matching is symmetric, so both sides get "query: " — the prefix the E5
model card recommends for symmetric tasks (STS, paraphrase, clustering).
Discovery's retrieval path uses "query: " / "passage: " instead; do not mix
the two conventions, the spaces are different.
"""

import time

import numpy as np
import requests

from harmony_api.core.settings import get_settings

settings = get_settings()

QUERY_PREFIX = "query: "
BATCH_SIZE = 256
TIMEOUT_SECONDS = 120
RETRIES = 3

_session = requests.Session()
_session.mount("http://", requests.adapters.HTTPAdapter(pool_connections=4, pool_maxsize=8))
_session.mount("https://", requests.adapters.HTTPAdapter(pool_connections=4, pool_maxsize=8))


def get_embed_url() -> str | None:
    """Accept either a base URL or a full endpoint URL (mirrors Discovery's client)."""
    url = (settings.HARMONY_E5_EMBEDDER_URL or "").strip().rstrip("/")
    if not url:
        return None
    if "/text/" not in url:
        url = f"{url}/text/embed"
    return url


def is_configured() -> bool:
    return get_embed_url() is not None


def get_delosis_e5_embeddings(texts: list[str]) -> np.ndarray:
    """
    :param texts: List of texts.

    Get E5 embeddings from the Delosis embedding service. Vectors come back
    L2-normalised by the service, matching what sentence-transformers returns
    for the in-process models, so the library's cosine maths is unchanged.
    """

    if not texts:
        return np.array([])

    url = get_embed_url()
    if url is None:
        raise RuntimeError("HARMONY_E5_EMBEDDER_URL is not configured")

    headers = {}
    token = (settings.HARMONY_E5_EMBEDDER_TOKEN or "").strip()
    if token:
        headers["Authorization"] = f"Bearer {token}"

    vectors: list[list[float]] = []
    for start in range(0, len(texts), BATCH_SIZE):
        chunk = [QUERY_PREFIX + (t or "") for t in texts[start:start + BATCH_SIZE]]
        # prefix="" tells the service not to add its own prefix on top of ours.
        payload = {"texts": chunk, "prefix": ""}
        last_error: Exception | None = None
        for attempt in range(RETRIES):
            try:
                response = _session.post(
                    url, json=payload, headers=headers, timeout=TIMEOUT_SECONDS
                )
                response.raise_for_status()
                data = response.json()
                chunk_vectors = data.get("vectors") or data.get("embeddings")
                if chunk_vectors is None or len(chunk_vectors) != len(chunk):
                    raise RuntimeError(
                        f"Embedding service returned {0 if chunk_vectors is None else len(chunk_vectors)} "
                        f"vectors for {len(chunk)} texts"
                    )
                vectors.extend(chunk_vectors)
                last_error = None
                break
            except (requests.ConnectionError, requests.Timeout, RuntimeError) as e:
                last_error = e
                if attempt < RETRIES - 1:
                    time.sleep(0.5 * (2 ** attempt))
        if last_error is not None:
            raise last_error

    return np.asarray(vectors, dtype=np.float32)
