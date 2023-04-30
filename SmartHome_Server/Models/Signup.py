from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    email: str
    password: str
    age: Optional[float] = None
    address: str