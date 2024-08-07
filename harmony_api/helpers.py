"""
MIT License

Copyright (c) 2023 Ulster University (https://www.ulster.ac.uk).
Project: Harmony (https://harmonydata.ac.uk)
Maintainer: Thomas Wood (https://fastdatascience.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import json
import os
from typing import List

import numpy as np

from harmony.schemas.requests.text import Instrument, Question
from harmony_api.core.settings import get_settings
from harmony_api.services.openai_embeddings import (
    HARMONY_API_AVAILABLE_OPENAI_MODELS_LIST,
)
from harmony_api.services.google_embeddings import (
    HARMONY_API_AVAILABLE_GOOGLE_MODELS_LIST,
)
from harmony_api.services.hugging_face_embeddings import (
    HUGGINGFACE_MPNET_BASE_V2,
    HUGGINGFACE_MINILM_L12_V2,
)
from harmony_api.services.azure_openai_embeddings import (
    HARMONY_API_AVAILABLE_AZURE_OPENAI_MODELS_LIST,
)

settings = get_settings()

dir_path = os.path.dirname(os.path.realpath(__file__))


def get_example_instruments() -> List[Instrument]:
    """Get example instruments"""

    example_instruments = []

    with open(
        str(os.getcwd()) + "/example_questionnaires.json", "r", encoding="utf-8"
    ) as file:
        for line in file:
            instrument = Instrument.parse_raw(line)
            example_instruments.append(instrument)

    return example_instruments


def get_mhc_embeddings(model_name: str) -> tuple:
    """Get mhc embeddings"""

    mhc_questions = []
    mhc_all_metadata = []
    mhc_embeddings = np.zeros((0, 0))

    # Only return the MHC embeddings for the Hugging Face models
    if model_name not in [
        HUGGINGFACE_MPNET_BASE_V2["model"],
        HUGGINGFACE_MINILM_L12_V2["model"],
    ]:
        return mhc_questions, mhc_all_metadata, mhc_embeddings

    try:
        data_path = os.path.join(dir_path, "../mhc_embeddings")  # submodule

        with open(
            os.path.join(data_path, "mhc_questions.txt"), "r", encoding="utf-8"
        ) as file:
            for line in file:
                mhc_question = Question(question_text=line)
                mhc_questions.append(mhc_question)

        with open(
            os.path.join(data_path, "mhc_all_metadatas.json"), "r", encoding="utf-8"
        ) as file:
            for line in file:
                mhc_meta = json.loads(line)
                mhc_all_metadata.append(mhc_meta)

        with open(
            os.path.join(
                data_path, f"mhc_embeddings_{model_name.replace('/', '-')}.npy"
            ),
            "rb",
        ) as file:
            mhc_embeddings = np.load(file, allow_pickle=True)
    except (Exception,) as e:
        print(f"Could not load MHC embeddings {str(e)}")

    return mhc_questions, mhc_all_metadata, mhc_embeddings


def check_model_availability(model: dict) -> bool:
    """
    Check model availability.
    """

    # Hugging Face
    if model["framework"] == "huggingface":
        # No checks required, always return True at the end of this function
        pass

    # OpenAI
    elif model["framework"] == "openai":
        if not settings.OPENAI_API_KEY:
            return False

        # Check model
        if model["model"] not in HARMONY_API_AVAILABLE_OPENAI_MODELS_LIST:
            return False

    # Azure OpenAI
    elif model["framework"] == "azure_openai":
        # Check model
        if model["model"] not in HARMONY_API_AVAILABLE_AZURE_OPENAI_MODELS_LIST:
            return False

    # Google
    elif model["framework"] == "google":
        if not settings.GOOGLE_APPLICATION_CREDENTIALS:
            return False

        # Check model
        if model["model"] not in HARMONY_API_AVAILABLE_GOOGLE_MODELS_LIST:
            return False

    return True
