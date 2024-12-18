from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

users = {'1': 'Имя: Example, возраст: 18'}

app = FastAPI()

@app.get('/')
async def main_page() -> str:
    return 'Main page'

@app.get('/users')
async def get_all_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def post_user(username:Annotated[str, Path(..., min_length=5, max_length=20)]
                    , age:Annotated[int, Path(..., ge=18, le=120)]) -> str:
    idx = str(int(max(users, key=int)) + 1)
    users[idx] = f'Имя: {username}, возраст: {age}'
    return f'User {idx} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def put_user(user_id:str, username:Annotated[str, Path(..., min_length=5, max_length=20)]
                    , age:Annotated[int, Path(..., ge=18, le=120)]) -> str:
    try:
        users[user_id]
        users[user_id] = f'Имя: {username}, возраст: {age}'
        return f'The user {user_id} is updated'
    except KeyError:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

@app.delete('/user/{user_id}')
async def delete_user(user_id:str) -> str:
    try:
        users.pop(user_id)
        return f'The user {user_id} is updated'
    except KeyError:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
