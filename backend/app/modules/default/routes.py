from fastapi import status, Depends, HTTPException,\
    APIRouter
from fastapi.security import OAuth2PasswordBearer
# from fake import fake_users_db
from tools import paginate_parameters
from typing import Union
from config import settings
from sqlmodel import Session, select
from fastapi.security import OAuth2PasswordRequestForm
from tools import digest

Tb = settings.app.Tb
engine = settings.engine

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/default",
    tags=["default"],
    dependencies=[Depends(oauth2_scheme)],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def read_root():
    return {"api": "/docs","message":"please visit localhost/docs to interact with api"}

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # getting the user
    with Session(engine) as session:
        res = select(Tb.User).filter(Tb.User.correo == form_data.username)
        user = session.exec(res).first()
        if user is None:
            HTTPException(status_code=404, detail='Usuario no encontrado')
    if digest(form_data.password) != user.password:
        raise HTTPException(
            status_code=400, detail="Usuario o contraseña equivocada")

    return {"access_token": user.correo, "token_type": "bearer"}