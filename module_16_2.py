from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def get_main():
    return 'Главная страница'

@app.get("/user/{user_id}")
async def get_user_by_id(user_id:Annotated[int, Path(..., ge=1, le=100, description='Enter User ID')]):
    return f'Вы вошли как пользователь № {user_id}'

@app.get("/user/{username}/{age}")
async def get_user_by_name(username:Annotated[str, Path(..., min_length=5, max_length=20)]
                           , age:Annotated[int, Path(..., ge=18, le=120)]):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
