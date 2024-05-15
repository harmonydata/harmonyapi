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

import os
from typing import List

import harmony
from fastapi import APIRouter, status
from harmony_api.constants import ALL_MODELS
from harmony_api.helpers import check_model_availability

router = APIRouter(prefix="/info")


@router.get(path="/version", status_code=status.HTTP_200_OK)
def show_version():
    """
    Show version.
    """

    return {
        "version_id": os.environ.get("COMMIT_ID", "Unknown"),
        "harmony_version": harmony.__version__,
    }


@router.get(
    path="/list-models", status_code=status.HTTP_200_OK, response_model=List[dict]
)
def show_models() -> List[dict]:
    """
    Show models.
    """

    models = []
    for model in ALL_MODELS:
        is_available = check_model_availability(model)
        model_dict = {**model, "available": is_available}
        models.append(model_dict)

    return models
