import json
import os
from typing import List

from harmony.schemas.requests.text import Instrument

import constants
from utils.singleton_meta import SingletonMeta

data_path = os.getenv("HARMONY_DATA_PATH", os.getcwd())
cache_file_path = os.path.join(data_path, constants.INSTRUMENTS_CACHE_JSON_FILENAME)


class InstrumentsCache(metaclass=SingletonMeta):
    """
    This class is responsible for caching instruments (Singleton class)
    """

    def __init__(self):
        self.__cache: dict[str, List[Instrument]] = {}

        self.__load()

    def __load(self):
        """Load cache"""

        if os.path.isfile(cache_file_path):
            with open(cache_file_path, "r", encoding="utf8") as file:
                cache = json.loads(file.read())
        else:
            cache = {}

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

    def get_cache(self) -> dict[str, List[Instrument]]:
        """Get the whole cache"""

        return self.__cache

    def save(self):
        """Save cache"""

        # Parse the cache
        cache_parsed: dict[str, List] = {}
        for key, value in self.__cache.items():
            instruments = [x.dict() for x in value]
            cache_parsed[key] = instruments

        # Save
        with open(cache_file_path, "w", encoding="utf8") as file:
            file.write(json.dumps(cache_parsed, ensure_ascii=False))

        print(f"INFO:\t  Cache {constants.INSTRUMENTS_CACHE_JSON_FILENAME} saved...")
