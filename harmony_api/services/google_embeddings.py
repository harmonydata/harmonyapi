import base64
import json
import os

import numpy as np
import vertexai
from google.oauth2.service_account import Credentials
from vertexai.language_models import TextEmbeddingInput, TextEmbeddingModel

from harmony_api.constants import GOOGLE_GECKO_003, GOOGLE_GECKO_MULTILINGUAL
from harmony_api.core.settings import get_settings

settings = get_settings()

# Authenticate Vertex AI with Google service account
if settings.GOOGLE_APPLICATION_CREDENTIALS:
    credentials = Credentials.from_service_account_info(
        settings.GOOGLE_APPLICATION_CREDENTIALS,
        scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )
    vertexai.init(
        project=settings.GOOGLE_APPLICATION_CREDENTIALS["project_id"],
        credentials=credentials,
    )


def __get_google_embeddings(texts: list[str], model_name: str) -> np.ndarray:
    """
    :param texts: List of texts.
    :param model_name: The model name.

    Get Google embeddings.
    """

    if not texts:
        return np.array([])

    model = TextEmbeddingModel.from_pretrained(model_name)
    inputs = [
        TextEmbeddingInput(text=text, task_type="RETRIEVAL_DOCUMENT") for text in texts
    ]
    embeddings = model.get_embeddings(inputs)

    return np.array([embedding.values for embedding in embeddings], dtype="float32")


def get_google_embeddings_gecko_003(texts: list[str]) -> np.ndarray:
    """
    :param texts: List of texts.

    Get Google embeddings.
    """

    return __get_google_embeddings(texts=texts, model_name=GOOGLE_GECKO_003["model"])


def get_google_embeddings_gecko_multilingual(texts: list[str]) -> np.ndarray:
    """
    :param texts: List of texts.

    Get Google embeddings.
    """

    return __get_google_embeddings(
        texts=texts, model_name=GOOGLE_GECKO_MULTILINGUAL["model"]
    )
