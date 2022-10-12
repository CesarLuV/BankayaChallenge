'''Base model for input post API.'''

from pydantic import BaseModel
from typing import List


class Location(BaseModel):
    locations: List[str]
