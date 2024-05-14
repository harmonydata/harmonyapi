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
from harmony.schemas.model import Model
from harmony.schemas.requests.text import Instrument, Question


def get_example_instruments() -> List[Instrument]:
    """
    Get example instruments.
    """

    example_instruments = []

    with open(
        str(os.getcwd()) + "/example_questionnaires.json", "r", encoding="utf-8"
    ) as file:
        for line in file:
            instrument = Instrument.parse_raw(line)
            example_instruments.append(instrument)

    return example_instruments


def get_mhc_embeddings(model: Model) -> tuple:
    """
    :param model: The model.

    Get MHC embeddings.
    """

    mhc_questions = []
    mhc_all_metadata = []
    mhc_embeddings = np.zeros((0, 0))

    # Only return the MHC embeddings for the Hugging Face models
    if (
        model.name != "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        or model.name != "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
    ):
        return mhc_questions, mhc_all_metadata, mhc_embeddings

    # Submodule
    data_path = "mhc_embeddings"

    # Get MHC questions
    with open(
        os.path.join(data_path, "mhc_questions.txt"), "r", encoding="utf-8"
    ) as file:
        for line in file:
            mhc_question = Question(question_text=line)
            mhc_questions.append(mhc_question)

    # Get MHC metadata
    with open(
        os.path.join(data_path, "mhc_all_metadatas.json"), "r", encoding="utf-8"
    ) as file:
        for line in file:
            mhc_meta = json.loads(line)
            mhc_all_metadata.append(mhc_meta)

    # Get MHC embeddings
    with open(
        os.path.join(data_path, f"mhc_embeddings_{model.name.replace('/', '-')}.npy"),
        "rb",
    ) as file:
        mhc_embeddings = np.load(file, allow_pickle=True)

    return mhc_questions, mhc_all_metadata, mhc_embeddings
