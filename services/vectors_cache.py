'''
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

'''

import json
import os
from typing import List

import constants
from utils.singleton_meta import SingletonMeta

data_path = os.getenv("HARMONY_DATA_PATH", os.getcwd())
cache_file_path = os.path.join(data_path, constants.VECTORS_CACHE_JSON_FILENAME)


class VectorsCache(metaclass=SingletonMeta):
    """
    This class is responsible for caching vectors (Singleton class)
    """

    def __init__(self):
        self.__cache: dict[str, dict[str, List[float]]] = {}

        self.__load()

    def __load(self):
        """Load cache"""

        if os.path.isfile(cache_file_path):
            with open(cache_file_path, "r", encoding="utf8") as file:
                cache = json.loads(file.read())
        else:
            cache = {}

        self.__cache = cache

    def set(self, key: str, value: dict[str, List[float]]):
        """Set key value pair"""

        self.__cache[key] = value

    def get(self, key: str) -> dict[str, List[float]]:
        """Get value by key"""

        return self.__cache.get(key)

    def has(self, key: str) -> bool:
        """Check if key is in cache"""

        return key in self.__cache

    def get_cache(self) -> dict[str, dict[str, List[float]]]:
        """Get the whole cache"""

        return self.__cache

    def save(self):
        """Save cache"""

        # Save
        with open(cache_file_path, "w", encoding="utf8") as file:
            file.write(json.dumps(self.__cache, ensure_ascii=False))

        print(f"INFO:\t  Cache {constants.VECTORS_CACHE_JSON_FILENAME} saved...")
