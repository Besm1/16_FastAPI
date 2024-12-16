from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

# Создаем экземпляр приложения FastAPI
app = FastAPI()

@app.post("/item/")
async def create_item(item: Item):
    return {"name": item.name, "price": item.price}

# Определение базового маршрута
@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

@app.get("/main")
async def main_page():
    return {"message": 'Main page'}
