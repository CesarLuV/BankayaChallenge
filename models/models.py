from pydantic import BaseModel
from typing import List

class Location(BaseModel):
    locations: List[str]
