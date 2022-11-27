from config import settings
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

app = settings.app
Tb = app.Tb

usr = {}


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = usr.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = usr(**user_dict)
    hashed_password = usr(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}
