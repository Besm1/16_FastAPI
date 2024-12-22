from fastapi import FastAPI, Path, Request, HTTPException
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from pydantic import BaseModel, Field
from fastapi.templating import Jinja2Templates

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
templates = Jinja2Templates(directory='templates')


users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/", response_class=HTMLResponse)
async def get_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get('/user/{user_id}', response_class=HTMLResponse)
async def user_details(request: Request, user_id:int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request":request, "user":users[user_id]})
    except KeyError:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

@app.post('/user/{username}/{age}')
async def post_user(username:Annotated[str, Path(..., min_length=5, max_length=20)]
                    , age:Annotated[int, Path(..., ge=18, le=120)]) -> str:
    idx = max((u_.id for u_ in users) , default=0) + 1
    users.append(User(id=idx, username=username, age=age))
    return f'User {idx} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def put_user(user_id:int, username:Annotated[str, Path(..., min_length=5, max_length=20)]
                    , age:Annotated[int, Path(..., ge=18, le=120)]) -> str:
    for u in users:
        if u.id == user_id:
            u.username = username
            u.age = age
            return f'User {user_id} is updated'
    raise HTTPException(status_code=404, detail=f"User {user_id} not found")

@app.delete('/user/{user_id}')
async def delete_user(user_id:int) -> str:
    for i, u in enumerate(users):
        if u.id == user_id:
            del users[i]
            return f'User {user_id} is deleted'
    raise HTTPException(status_code=404, detail=f"User {user_id} not found")
