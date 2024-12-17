from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def get_main():
    return 'Главная страница'

@app.get("/user/{user_id}")
async def get_user_by_id(user_id:Annotated[int, Path(..., ge=1, le=100, description='Enter User ID')]):
    return f'Вы вошли как пользователь № {user_id}'

@app.get("/user")
async def get_user_by_name(username:str, age:int):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
