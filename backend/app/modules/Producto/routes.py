from fastapi import status, Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordBearer

# from fake import fake_users_db
from tools import paginate_parameters
from typing import Union, List
from config import settings
from sqlmodel import Session, select

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/Producto",
    tags=["Producto"],
    dependencies=[Depends(oauth2_scheme)],
    responses={404: {"description": "Not found"}},
)


Tb = settings.app.Tb
engine = settings.engine

@router.post('/', response_model=Tb.Producto, status_code=status.HTTP_201_CREATED)
def registrar_producto(product: Tb.Producto):
    with Session(engine) as session:
        session.add(product)
        session.commit()
        session.refresh(product)
    return product


@router.put(
    "/{product_id}", response_model=Tb.Producto, status_code=status.HTTP_202_ACCEPTED
)
def modificar_producto(product_id: int, productnew: Tb.ProductoModify):
    with Session(engine) as session:
        res = select(Tb.Producto).filter(Tb.Producto.id == product_id)
        product = session.exec(res).one()
        for key in productnew.__fields__:
            if hasattr(product,key):
                setattr(product,key, getattr(productnew, key))
        session.add(product)
        session.commit()
        session.refresh(product)
    return product
