from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# class Item(BaseModel):
#     item_id: int
#     name:str
#     age:int
#     address: Optional[str] = None

# data ={}

# @app.post("/items/")
# def update_item(item:Item):

#     data["item_id"]=item.item_id
#     data["name"]=item.name
#     data["age"]=item.age
#     return data

# @app.get("/items/")
# def read_item():
    
#         return data


class Book(BaseModel):
    book_id: Optional[int] = None
    name: str
    price: str
    description: str
    image: Optional[str] = None
    rating: Optional[str] = None
 

# Update the create_book function to use book_id as an optional field
@app.post("/books/")
def create_book(book: Book):
    return {"book_id":book.book_id,"name":book.name,"price":book.price,"description":book.description}
   