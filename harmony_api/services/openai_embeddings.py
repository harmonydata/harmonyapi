import os

import numpy as np
import openai

from harmony_api.constants import OPENAI_3_LARGE, OPENAI_ADA_02

# OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY", "")


def __get_openai_embeddings(texts: list[str], model_name: str) -> np.ndarray:
    """
    :param texts: List of texts.
    :param model_name: The model name.

    Get OpenAI embeddings.
    """

    res = openai.embeddings.create(
        input=texts,
        model=model_name,
    )

    embeddings = [r.embedding for r in res.data]

    return np.array(embeddings, dtype="float32")


def get_openai_embeddings_3_large(texts: list[str]) -> np.ndarray:
    """
    :param texts: List of texts.

    Get OpenAI embeddings.
    """

    return __get_openai_embeddings(texts=texts, model_name=OPENAI_3_LARGE["model"])


def get_openai_embeddings_ada_02(texts: list[str]) -> np.ndarray:
    """
    :param texts: List of texts.

    Get OpenAI embeddings.
    """

    return __get_openai_embeddings(texts=texts, model_name=OPENAI_ADA_02["model"])
