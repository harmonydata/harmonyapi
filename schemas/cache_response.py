from typing import List

from harmony.schemas.requests.text import Instrument
from pydantic import BaseModel, Field


class CacheResponse(BaseModel):
    instruments: List[Instrument] = Field(description="A list of instruments")
    vectors: List[dict] = Field(description="A list of vectors")
