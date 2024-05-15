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

INSTRUMENTS_CACHE_JSON_FILENAME = "instruments_cache.json"
VECTORS_CACHE_JSON_FILENAME = "vectors_cache.json"

# Models
HUGGINGFACE_MINILM_L12_V2 = {
    "framework": "huggingface",
    "model": "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    "available": True,
}

HUGGINGFACE_MPNET_BASE_V2 = {
    "framework": "huggingface",
    "model": "sentence-transformers/paraphrase-multilingual-mpnet-base-v2",
    "available": True,
}
OPENAI_ADA_02 = {
    "framework": "openai",
    "model": "text-embedding-ada-002",
    "available": True,
}

OPENAI_3_LARGE = {
    "framework": "openai",
    "model": "text-embedding-3-large",
    "available": True,
}

GOOGLE_GECKO_003 = {
    "framework": "google",
    "model": "textembedding-gecko@003",
    "available": True,
}

GOOGLE_GECKO_MULTILINGUAL = {
    "framework": "google",
    "model": "textembedding-gecko-multilingual",
    "available": True,
}

# All available models
AVAILABLE_MODELS: list[dict] = [
    HUGGINGFACE_MINILM_L12_V2,
    HUGGINGFACE_MPNET_BASE_V2,
    OPENAI_ADA_02,
    OPENAI_3_LARGE,
    GOOGLE_GECKO_003,
    GOOGLE_GECKO_MULTILINGUAL,
]

AVAILABLE_MODELS_NAMES = [x["model"] for x in AVAILABLE_MODELS]
AVAILABLE_MODELS_FRAMEWORKS = [x["framework"] for x in AVAILABLE_MODELS]
