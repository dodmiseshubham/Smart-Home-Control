from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
 
app = FastAPI()
 
@app.get("/")
def root ():
  return {"message": "Hello World!"}

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.post("/items/")
async def create_item(item: Item):
    print("Item ",item)
    return item

