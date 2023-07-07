from typing import List

from harmony.schemas.requests.text import Instrument

import constants
from utils import cache_helper
from utils.singleton_meta import SingletonMeta


class InstrumentsCache(metaclass=SingletonMeta):
    """
    This class is responsible for caching instruments (Singleton class)
    """

    def __init__(self):
        self.__cache: dict[str, List[Instrument]] = {}

        self.__load()

    def __load(self):
        """Load cache"""

        cache = cache_helper.get_cache_from_azure(
            constants.INSTRUMENTS_CACHE_JSON_FILENAME
        )

        # Parse the cache
        cache_parsed: dict[str, List[Instrument]] = {}
        for key, value in cache.items():
            instruments = [Instrument.parse_obj(x) for x in value]
            cache_parsed[key] = instruments

        self.__cache = cache_parsed

    def set(self, key: str, value: List[Instrument]):
        """Set key value pair"""

        self.__cache[key] = value

    def get(self, key: str) -> List[Instrument]:
        """Get value by key"""

        return self.__cache.get(key)

    def has(self, key: str) -> bool:
        """Check if key is in cache"""

        return key in self.__cache

    def get_all(self) -> dict[str, List[Instrument]]:
        """Get the whole cache"""

        return self.__cache

    def save(self):
        """Save cache to Azure Blob Storage"""

        # Parse the cache
        cache_parsed: dict[str, List] = {}
        for key, value in self.__cache.items():
            instruments = [x.dict() for x in value]
            cache_parsed[key] = instruments

        cache_helper.save_cache_to_azure(
            cache=cache_parsed,
            cache_file_name=constants.INSTRUMENTS_CACHE_JSON_FILENAME,
        )
