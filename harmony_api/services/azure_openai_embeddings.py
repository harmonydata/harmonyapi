import numpy as np
import openai
from openai import AzureOpenAI

from harmony_api.constants import (
    AZURE_OPENAI_3_LARGE,
    AZURE_OPENAI_ADA_02,
    HARMONY_API_AZURE_OPENAI_MODELS_LIST,
)
from harmony_api.core.settings import get_settings
from typing import List

settings = get_settings()

API_VERSION = "2023-12-01-preview"  # This might change in the future

# Check available models
print("INFO:\t  Checking Azure OpenAI models...")
HARMONY_API_AVAILABLE_AZURE_OPENAI_MODELS_LIST: List[str] = []
if settings.AZURE_OPENAI_API_KEY and settings.AZURE_OPENAI_ENDPOINT:
    for harmony_api_azure_openai_model in HARMONY_API_AZURE_OPENAI_MODELS_LIST:
        try:
            AzureOpenAI(
                api_key=settings.AZURE_OPENAI_API_KEY,
                api_version=API_VERSION,
                base_url=f"{settings.AZURE_OPENAI_ENDPOINT}/openai/deployments/{harmony_api_azure_openai_model['model']}",
            ).embeddings.create(
                model=harmony_api_azure_openai_model["model"], input=["test"]
            )
            HARMONY_API_AVAILABLE_AZURE_OPENAI_MODELS_LIST.append(
                harmony_api_azure_openai_model["model"]
            )
        except openai.NotFoundError:
            pass


def __get_azure_openai_embeddings(texts: list[str], model_name: str) -> np.ndarray:
    """
    :param texts: List of texts.
    :param model_name: The model name.

    Get Azure OpenAI embeddings.
    """

    if not texts:
        return np.array([])

    client = AzureOpenAI(
        api_key=settings.AZURE_OPENAI_API_KEY,
        api_version=API_VERSION,  # This might change in the future
        base_url=f"{settings.AZURE_OPENAI_ENDPOINT}/openai/deployments/{model_name}",
    )

    res = client.embeddings.create(model=model_name, input=texts)

    embeddings = [r.embedding for r in res.data]

    return np.array(embeddings, dtype="float32")


def get_azure_openai_embeddings_3_large(texts: list[str]) -> np.ndarray:
    """
    :param texts: List of texts.

    Get OpenAI embeddings.
    """

    return __get_azure_openai_embeddings(
        texts=texts, model_name=AZURE_OPENAI_3_LARGE["model"]
    )


def get_azure_openai_embeddings_ada_02(texts: list[str]) -> np.ndarray:
    """
    :param texts: List of texts.

    Get OpenAI embeddings.
    """

    return __get_azure_openai_embeddings(
        texts=texts, model_name=AZURE_OPENAI_ADA_02["model"]
    )
