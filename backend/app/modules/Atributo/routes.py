from fastapi import status, Depends, HTTPException,\
    APIRouter
from fastapi.security import OAuth2PasswordBearer
# from fake import fake_users_db
from tools import paginate_parameters
from typing import Union
from config import settings
from sqlmodel import Session, select

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/Atributo",
    tags=["Atributo"],
    dependencies=[Depends(oauth2_scheme)],
    responses={404: {"description": "Not found"}},
)