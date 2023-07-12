import json
import os
from typing import List

import constants
from utils.singleton_meta import SingletonMeta

data_path = os.path.join(os.getenv("HARMONY_DATA_PATH", "data"))
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
