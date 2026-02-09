from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# This defines the structure of data we expect
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

@app.get("/")
async def root():
    return {"status": "online", "message": "Python API is running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# NEW: POST endpoint to receive data
@app.post("/items")
async def create_item(item: Item):
    # In a real application, you would save the item to a database here
    return {"message": "Item created successfully", "data": item}