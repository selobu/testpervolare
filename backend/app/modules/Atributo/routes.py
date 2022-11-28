from fastapi import status, Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordBearer

# from fake import fake_users_db
from tools import paginate_parameters, force_check
from typing import Union
from config import settings
from sqlmodel import Session, select
from typing import List

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/Atributo",
    tags=["Atributo"],
    dependencies=[Depends(oauth2_scheme)],
    responses={404: {"description": "Not found"}},
)

Tb = settings.app.Tb
engine = settings.engine

@router.post("/", response_model=Tb.Atributo, status_code=status.HTTP_201_CREATED)
def registrar_atributo(atributo: Tb.Atributo):
    with Session(engine) as session:
        # TODO
        # report a bug happends when default field is not set and then the field.validator didn't run
        atributo = force_check(atributo, b.Atributo)
        # TODO-END
        session.add(atributo)
        session.commit()
        session.refresh(atributo)
    return atributo


@router.put(
    "/{atribute_id}", response_model=Tb.Atributo, status_code=status.HTTP_202_ACCEPTED
)
def modificar_atributo(atribute_id: str, productnew: Tb.Atributo):
    with Session(engine) as session:
        res = select(Tb.Atributo).filter(Tb.Atributo.id == atribute_id)
        atributo = session.exec(res).one()
        for key in productnew.__fields__:
            if hasattr(atributo, key):
                setattr(atributo, key, getattr(productnew, key))
        session.add(atributo)
        session.commit()
        session.refresh(atributo)
    return atributo


@router.get(
    "/{atribute_id}", response_model=Tb.Atributo, status_code=status.HTTP_202_ACCEPTED
)
def leer_atributo(atribute_id: str):
    with Session(engine) as session:
        res = select(Tb.Atributo).filter(Tb.Atributo.id == atribute_id)
        atributo = session.exec(res).one()
        return atributo


@router.get("/", response_model=List[Tb.Atributo], status_code=status.HTTP_202_ACCEPTED)
def leer_atributos():
    with Session(engine) as session:
        res = select(Tb.Atributo)
        atributos = session.exec(res).all()
        return atributos


@router.delete("/{atribute_id}",status_code=status.HTTP_200_OK)
def eliminar_atributo(atribute_id: str):
    with Session(engine) as session:
        res = select(Tb.Atributo).filter(Tb.Atributo.id == atribute_id)
        atributo = session.exec(res).one()
        session.delete(atributo)
        session.commit()
