from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World."}


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
async def create_item(item: Item):
   item_dict = item.dict()
   if item.tax:
       price_with_tax = item.price = item.tax
       item_dict.update({"price_with_tax": price_with_tax })
   return item_dict

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str = None):
    '''
	item_id : path param
        item : request body
        q : quary param
'''
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

from fastapi import Query

@app.get("/items")
async def read_items(q: str = Query(None, max_length=50, min_length=3, regex="^\w+"))
'''
	None: default value of q
        max_length: max length of q
        regex: regular expressions
        min_length: min length of q
'''
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
