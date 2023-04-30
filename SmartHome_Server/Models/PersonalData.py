from typing import Optional
from pydantic import BaseModel

class personalData(BaseModel):
    roomTemprature: str
    roomHumidity: str