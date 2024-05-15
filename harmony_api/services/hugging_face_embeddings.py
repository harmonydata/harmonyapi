import numpy as np
from sentence_transformers import SentenceTransformer

from harmony_api.constants import HUGGINGFACE_MINILM_L12_V2, HUGGINGFACE_MPNET_BASE_V2

# Load Hugging Face sentence transformers
model_huggingface_minilm_l12_v2 = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)
model_huggingface_mpnet_base_v2 = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
)


def __get_hugging_face_embeddings(texts: list[str], model_name: str) -> np.ndarray:
    """
    :param texts: List of texts.
    :param model_name: The model name.

    Get Hugging Face embeddings.
    """

    if not texts:
        return np.array([])

    embeddings = []

    if model_name == HUGGINGFACE_MINILM_L12_V2["model"]:
        embeddings = model_huggingface_minilm_l12_v2.encode(
            sentences=texts, convert_to_numpy=True
        )
    elif model_name == HUGGINGFACE_MPNET_BASE_V2["model"]:
        embeddings = model_huggingface_mpnet_base_v2.encode(
            sentences=texts, convert_to_numpy=True
        )

    return embeddings


def get_hugging_face_embeddings_mpnet_base_v2(texts: list[str]) -> np.ndarray:
    """
    :param texts: List of texts.

    Get Hugging Face embeddings.
    """

    return __get_hugging_face_embeddings(
        texts=texts, model_name=HUGGINGFACE_MPNET_BASE_V2["model"]
    )


def get_hugging_face_embeddings_minilm_l12_v2(texts: list[str]) -> np.ndarray:
    """
    :param texts: List of texts.

    Get Hugging Face embeddings.
    """

    return __get_hugging_face_embeddings(
        texts=texts, model_name=HUGGINGFACE_MINILM_L12_V2["model"]
    )
