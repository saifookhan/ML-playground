from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import urllib
import json

from lib.weaviate_helper import query_from_db

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

#{"CATEGORY": "CONTEXT"}
possible_query = [{"SPORTS": "America"}, {"BUSINESS": "germany"}]

@app.get("/")
def read_root():
    
    params = json.dumps(possible_query)
    final_url = str("example.com") + "&q=" + str(params)
    return {"Hello": final_url}


@app.get("/get/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/getAudio")
def get_audio(q: Union[str, None] = None):
    print(q)
    print(query_from_db(q))
    return {"q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}