from typing import List

import constants
from utils import cache_helper
from utils.singleton_meta import SingletonMeta


class VectorsCache(metaclass=SingletonMeta):
    """
    This class is responsible for caching vectors (Singleton class)
    """

    def __init__(self):
        self.__cache: dict[str, dict[str, List[float]]] = {}

        self.__load()

    def __load(self):
        """Load cache"""

        self.__cache = cache_helper.get_cache_from_azure(
            constants.VECTORS_CACHE_JSON_FILENAME
        )

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
        """Save cache to Azure Blob Storage"""

        cache_helper.save_cache_to_azure(
            cache=self.__cache,
            cache_file_name=constants.VECTORS_CACHE_JSON_FILENAME,
        )
