from fastapi import status, Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordBearer
from tools import paginate_parameters
from typing import Union, List
from config import settings
from pydantic import BaseModel
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/Users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)

Tb = settings.app.Tb
Pyd = settings.app.Pyd
engine = settings.engine


def regfromclass(value, clase: BaseModel):
    toset = [r for r in value.__fields__ if r in clase.__fields__]
    res = dict()
    for item in toset:
        res[item] = getattr(value, item)
    return clase(**res)


@router.post("/", response_model=Pyd.User, status_code=status.HTTP_201_CREATED)
async def registrar_user(user: Pyd.User):
    with Session(engine) as session:
        usr = regfromclass(user, Tb.User)
        login = regfromclass(user, Tb.Login)
        login.user = usr
        session.add(login)
        session.commit()
        session.refresh(usr)
    return usr
