from fastapi import status, Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordBearer

# from fake import fake_users_db
from tools import paginate_parameters
from typing import Union, List
from config import settings
from sqlmodel import Session, select

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/Users",
    tags=["Users"],
    dependencies=[Depends(oauth2_scheme)],
    responses={404: {"description": "Not found"}},
)


Tb = settings.app.Tb
engine = settings.engine


def get_user(email: str):
    with Session(engine) as session:
        res = select(Tb.User).filter(Tb.User.correo == email)
        res = session.exec(res).first()
        if res is not None:
            return res
        raise HTTPException(status_code=404, detail="Usuario no encontradp")


def fake_decode_token(token):
    user = get_user(token)
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticación inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(current_user: Tb.User = Depends(get_current_user)):
    if not current_user.activo:
        raise HTTPException(status_code=400, detail="Usuario inactivo")
    return current_user


@router.get("/")
async def read_all_user(
    commons: dict = Depends(paginate_parameters), token: str = Depends(oauth2_scheme)
):
    email = token
    limit = commons["limit"]
    with Session(engine) as session:
        res = select(Tb.User).limit(limit)
        res = session.exec(res).all()
    return res


@router.post("/", response_model=Tb.User, status_code=status.HTTP_201_CREATED)
async def registrar_user(user: Tb.User, token: str = Depends(oauth2_scheme)):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)  # updating the id
    return user
