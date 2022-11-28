from datetime import date
from typing import Optional
from tools import map_name_to_table

from sqlalchemy.orm import declarative_base, Mapped, mapped_column,\
    relationship
from sqlalchemy import String, Float, Date, ForeignKey
from uuid import uuid4
import re
from config import settings

Base = settings.Base

@map_name_to_table
class Producto(Base):
    __tablename__ = 'producto'
    id: Mapped[str] = mapped_column(default=uuid4, primary_key=True)
    name: Mapped[str] = mapped_column(String(10))
    value: Mapped[float] = mapped_column(Float)
    description: Mapped[str] = mapped_column(String(500))
    createDate: Mapped[date] = mapped_column(Date)
    updateDate: Mapped[date] = mapped_column(Date)
    softDelete: Mapped[date] = mapped_column(Date)


@map_name_to_table
class ProductAttribute(Base):
    __tablename__= 'productattribute'
    product_id: Mapped[str] = mapped_column(ForeignKey("producto.id"), primary_key=True)
    attribute_id: Mapped[str] = mapped_column(ForeignKey("atributo.id"), primary_key=True)
