from fastapi import FastAPI, HTTPException,Body
import json
from pydantic import BaseModel,Field
from typing import Optional,Dict,Any
import uvicorn


class  Description(BaseModel):
    upc: str | None = Field(None,alias="UPC")
    Product_type: str | None = Field(None,alias="Product_type")
    price_without_tax: str | None = Field(None,alias="Price (excl. tax)")
    Price_with_tax: str | None = Field(None,alias="Price (incl. tax)")
    tax: str | None = Field(None,alias="Tax")
    availability: str | None = Field(None,alias="Availability")
    no_of_reviews: str | None = Field(None,alias="Number of reviews")


class Book(BaseModel):
    book_id: int
    name: str
    price: str
    description: str
    image: str | None 
    rating: str | None 
    product_information: Optional[Description]

app = FastAPI()
filepath = '/Users/admin/Desktop/python training/final_project/books_detail.json'

def file_handler(data=None, mode='r'):
    with open(filepath, mode) as f:
        if mode.casefold() == 'r':
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return None          
        elif mode.casefold() == 'w':
            if data is not None:
                json.dump(data, f, indent=2)  # Convert data to a JSON string and write it
        else:
            raise Exception("UnKnown mode")
        
@app.get("/books")
def books(name: str = None,price: str = None,rating: str = None):
    book_list = []
    data=file_handler()
    for book in data:
        if name and name in book['name']: 
            book_list.append(book)
        if price and price in book["price"]:
            book_list.append(book)
        if rating and rating in book['rating']:
            book_list.append(book)
    if book_list:
        return book_list
    return data

@app.get("/books/{book_id}")
def book_details(book_id: int):
    data=file_handler()
    for book in data:
        if book["book_id"] == book_id:
            return book   
    raise HTTPException(status_code=404, detail="Book or book detail not found")

@app.post("/books/")
def create_book(book:Dict[Any,Any]):
    data=file_handler(mode='r')
    new_book ={}
    if data:
        last_book_id = max(item.get('book_id',0) for item in data)
        new_book['book_id'] = last_book_id +1
    else:
        new_book['book_id'] = 1
    new_book.update(book)
    
    data.append(new_book)

    file_handler(data,mode='w') 
    return {"message":"successfully data created"}

@app.patch("/books/{book_id}")
def update_book(book_id: int, book: Book):
    data = file_handler(mode='r')  
    for old_book in data:
        if old_book['book_id'] == book_id:
            if old_book['name']:
                old_book['name'] = book.name 
            if old_book['price']:
                old_book['price'] = book.price 
            file_handler(data, mode='w')
            return {"message":"successfully data updated"}
        
@app.delete("/books/")
def delete_book(book_id: int):
    data = file_handler(mode='r')
    update_new_data=list(filter(lambda book: book['book_id'] != book_id,data))     
    file_handler(data=update_new_data,mode='w')
    return {"message":"successfully data deleted"}


if __name__ == "__main__":

    uvicorn.run(app)



