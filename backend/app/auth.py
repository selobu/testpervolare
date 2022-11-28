from config import settings
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from tools import digest

app = settings.app
engine = settings.engine
Tb = app.Tb


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    email = form_data.username
    password = form_data.password
    with Session(settings.engine) as session:
        res = select(Tb.Login.password).filter(Tb.Login.email == email)
<<<<<<< HEAD
<<<<<<< HEAD
        currpass = session.exec(res).first()
=======
        currpass = session.execute(res).first()[0]
>>>>>>> 9af093b (fixing login)
=======
        currpass = session.execute(res).first()[0]
>>>>>>> 751ea766ead9c6788c40bfd5f8f3d0e8a395bca5
    if currpass is None:
        raise HTTPException(status_code=400, detail="Incorrect useremail or password")
    if digest(password) != currpass:
        raise HTTPException(status_code=400, detail="Invalid password")
    return {"access_token": email, "token_type": "bearer"}


@app.get("/")
def read_root():
    return {
        "api": "/docs",
        "message": "please visit localhost/docs to interact with api",
    }
