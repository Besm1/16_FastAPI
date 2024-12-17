from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_main():
    return 'Главная страница'

@app.get("/user/admin")
async def get_adm():
    return 'Вы вошли как администратор'

@app.get("/user/{user_id}")
async def get_user_by_id(user_id:int):
    return f'Вы вошли как пользователь № {user_id}'

@app.get("/user")
async def get_user_by_name(username:str, age:int):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
