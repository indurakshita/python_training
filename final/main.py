from fastapi import FastAPI, HTTPException
import json


app = FastAPI()


with open("books_detail.json", 'r') as file:
    book_details = json.load(file)
    
    

@app.get("/book_detail/{book_id}")
# async def get_book_price(book_id: str):
async def func(book_id: str):
    if book_id in book_details:
        return book_details[book_id]
    



    raise HTTPException(status_code=404, detail="Book or book detail not found")

