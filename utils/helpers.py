import json
import os
from typing import List

import numpy as np
from harmony.schemas.requests.text import Instrument, Question


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


def get_mhc_embeddings() -> tuple:
    """Get mhc embeddings"""

    mhc_questions = []
    mhc_all_metadata = []
    mhc_embeddings = np.zeros((0, 0))

    try:
        data_path = os.getenv("HARMONY_DATA_PATH", os.getcwd())
        with open(
            os.path.join(data_path, "mhc_questions.json"), "r", encoding="utf-8"
        ) as file:
            for line in file:
                mhc_question = Question.parse_raw(line)
                mhc_questions.append(mhc_question)
        with open(
            os.path.join(data_path, "mhc_all_metadatas.json"), "r", encoding="utf-8"
        ) as file:
            for line in file:
                mhc_meta = json.loads(line)
                mhc_all_metadata.append(mhc_meta)
        with open(os.path.join(data_path, "mhc_embeddings.npy"), "rb") as file:
            mhc_embeddings = np.load(file)
    except (Exception,) as e:
        print(f"Could not load MHC embeddings {str(e)}")

    return mhc_questions, mhc_all_metadata, mhc_embeddings
