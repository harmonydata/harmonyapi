import numpy as np
import openai
from openai import OpenAI

from harmony_api.constants import (
    HARMONY_API_OPENAI_MODELS_LIST,
    OPENAI_3_LARGE,
    OPENAI_ADA_02,
)
from harmony_api.core.settings import get_settings
from typing import List

settings = get_settings()

# OpenAI API key
if settings.OPENAI_API_KEY:
    openai.api_key = settings.OPENAI_API_KEY

# Check available models
print("INFO:\t  Checking OpenAI models...")
HARMONY_API_AVAILABLE_OPENAI_MODELS_LIST: List[str] = []
if settings.OPENAI_API_KEY:
    openai_client = OpenAI()
    OPENAI_MODELS: List[str] = [x.id for x in openai_client.models.list()]
    for harmony_api_openai_model in HARMONY_API_OPENAI_MODELS_LIST:
        if harmony_api_openai_model["model"] in OPENAI_MODELS:
            HARMONY_API_AVAILABLE_OPENAI_MODELS_LIST.append(
                harmony_api_openai_model["model"]
            )


def __get_openai_embeddings(texts: list[str], model_name: str) -> np.ndarray:
    """
    :param texts: List of texts.
    :param model_name: The model name.

    Get OpenAI embeddings.
    """

    if not texts:
        return np.array([])

    client = OpenAI()

    res = client.embeddings.create(
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
