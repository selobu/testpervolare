from fastapi import status, Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordBearer
from tools import paginate_parameters
from typing import Union, List
from config import settings
from sqlmodel import Session, select, SQLModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/Users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)

Tb = settings.app.Tb
engine = settings.engine


def regfromclass(value, clase: SQLModel):
    toset = [r for r in value.__fields__ if r in clase.__fields__]
    res = dict()
    for item in toset:
        res[item] = getattr(value, item)
    return clase(id=None, **res)


@router.post("/", response_model=Tb.User, status_code=status.HTTP_201_CREATED)
async def registrar_user(user: Tb.UserRegister):
    with Session(engine) as session:
        usr = regfromclass(user, Tb.User)
        login = regfromclass(user, Tb.Login)
        login.user = usr
        session.add(login)
        session.commit()
        session.refresh(login)
        print("/////--------Reading user -----------/////")
        print(login.user)
        return login.user
