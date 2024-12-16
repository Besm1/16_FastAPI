from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_main():
    return {'Главная страница'}

@app.get("/user/admin")
async def get_main():
    return {'Вы вошли как администратор'}

@app.get("/user/{user_id}")
async def get_main(user_id:int):
    return {f'Вы вошли как пользователь № {user_id}'}

@app.get("/user")
async def get_main(username:str, age:int):
    return {f'Информация о пользователе. Имя: {username}, Возраст: {age}'}



