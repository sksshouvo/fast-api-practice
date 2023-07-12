from typing import Union
from fastapi import FastAPI

my_awesome_api  = FastAPI()

@my_awesome_api.get("/")
async def read_root():
    return {"Hello": "World"}

@my_awesome_api.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}