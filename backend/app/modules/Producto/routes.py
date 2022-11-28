from fastapi import status, Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordBearer
from tools import paginate_parameters
from typing import Union, List
from config import settings
<<<<<<< HEAD
<<<<<<< HEAD
from sqlmodel import Session, select
=======
from sqlalchemy.orm import Session
from sqlalchemy import select
from pydantic import BaseModel
>>>>>>> a0471f2 (adjust system)
=======
from sqlalchemy.orm import Session
from sqlalchemy import select
from pydantic import BaseModel
>>>>>>> 751ea766ead9c6788c40bfd5f8f3d0e8a395bca5

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/Producto",
    tags=["Producto"],
    dependencies=[Depends(oauth2_scheme)],
    responses={404: {"description": "Not found"}},
)


Tb = settings.app.Tb
<<<<<<< HEAD
<<<<<<< HEAD
=======
Pyd = settings.app.Pyd
Base = settings.Base
>>>>>>> a0471f2 (adjust system)
=======
Pyd = settings.app.Pyd
Base = settings.Base
>>>>>>> 751ea766ead9c6788c40bfd5f8f3d0e8a395bca5
engine = settings.engine
u = lambda *args: args


<<<<<<< HEAD
def registrar_producto(product: Tb.Producto):
=======
def regfromclass(value, clase: Base):
    toset = dict((x,y) for x,y in list(value) if x in clase.metadata.tables[clase.__tablename__].columns.keys())
    res = dict()
    for item in toset:
        res[item] = getattr(value, item)
    return clase(**res)

def classfromreg(value: Base, clase: BaseModel):
    value_columns = value.metadata.tables[value.__tablename__].columns.keys()
    pydantyc_columns = clase.__fields__.keys()
    toset = [r for r in value_columns if r in pydantyc_columns]
    res = dict()
    for item in toset:
        res[item] = getattr(value, item)
    return clase(**res)

@router.post("/", response_model=Pyd.Producto, status_code=status.HTTP_201_CREATED)
def registrar_producto(product: Pyd.Producto):
>>>>>>> a0471f2 (adjust system)
    with Session(engine) as session:
        pd = regfromclass(product, Tb.Producto)
        session.add(pd)
        session.commit()
        session.refresh(pd)
        return classfromreg(pd, Pyd.Producto)


@router.put(
    "/{product_id}", response_model=Tb.Producto, status_code=status.HTTP_202_ACCEPTED
)
def modificar_producto(product_id: int, productnew: Tb.ProductoModify):
    with Session(engine) as session:
        res = select(Tb.Producto).filter(Tb.Producto.id == product_id)
        product = session.exec(res).one()
        for key in productnew.__fields__:
            if hasattr(product, key):
                setattr(product, key, getattr(productnew, key))
        session.add(product)
        session.commit()
        session.refresh(product)
    return product

@router.get("/{product_id}",response_model=Pyd.Producto, status_code=status.HTTP_202_ACCEPTED)
def get_product(product_id: int):
    with Session(engine) as session:
        res = select(Tb.Producto).filter(Tb.Producto.id == product_id)
        product = session.execute(res).one()
        return product

