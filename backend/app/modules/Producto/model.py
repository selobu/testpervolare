from datetime import date
from datetime import datetime
from typing import Optional
from tools import map_name_to_table, uuid_isvalid
from sqlmodel import Field, SQLModel, Column, String, Field, Float, Date, Integer
from pydantic import validator
from uuid import uuid4
import re
from config import settings

Base = settings.Base


@map_name_to_table
class Producto(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True, description="UUID 4")
    name: str = Field(
        unique=True,
        sa_column=Column(String(10)),
        max_length=10,
        min_length=2,
        description="Only alphanumeric values allowed",
    )
    value: float = Field(
        sa_column=Column(Float()), gt=0, le=9_999_999_999, description="Product value"
    )
    description: str = Field(
        sa_column=Column(String(500)),
        description="Product description. Only alphanumeric values",
        min_length=10,
        max_length=500,
    )
    createDate: Optional[date] = Field(
        sa_column=Column(Date()), description="Creation date"
    )
    updateDate: Optional[date] = Field(
        sa_column=Column(Date()), description="Update date"
    )
    softDelete: Optional[date] = Field(
        default=None, sa_column=Column(Date()), description="SoftDelete date"
    )

    @validator("id")
    def uuid_validator(cls, v):
        if v is not None:
            if not uuid_isvalid(v):
                raise ValueError("invalud uuid 4")
            return v
        else:
            return str(uuid4())

    @validator("name")
    def name_validator(cls, v):
        res = "".join(re.findall("([0-9]*[a-zA-Z]*[0-9]*)", v))
        if len(res) != len(v):
            raise ValueError("only allowed charactes and numerical values")
        return v

    @validator("value")
    def value_validator(cls, v):
        assert v > 0
        return v

    @validator("description")
    def desc_validator(cls, v):
        assert len(v) >= 10 and len(v) <= 500
        res = "".join(re.findall("([0-9]*[a-zA-Z]*[0-9]*)", v))
        if len(res) != len(v):
            raise ValueError("only allowed charactes and numerical values")
        return v



@map_name_to_table
class Producto(Base):
    __tablename__ = 'producto'
    id: Mapped[str] = mapped_column(default=uuid4, primary_key=True)
    name: Mapped[str] = mapped_column(String(10))
    value: Mapped[float] = mapped_column(Float)
    description: Mapped[str] = mapped_column(String(500))
    createDate: Mapped[Optional[date]] = mapped_column(Date, default=lambda x: date.today())
    updateDate: Mapped[date] = mapped_column(Date)
    softDelete: Mapped[date] = mapped_column(Date)


@map_name_to_table
<<<<<<< HEAD
class ProductAttribute(Base):
    __tablename__= 'productattribute'
    product_id: Mapped[str] = mapped_column(ForeignKey("producto.id"), primary_key=True)
    attribute_id: Mapped[str] = mapped_column(ForeignKey("atributo.id"), primary_key=True)
=======
class ProductoModify(SQLModel):
    name: str = Field(
        unique=True,
        sa_column=Column(String(10)),
        max_length=10,
        min_length=2,
        description="Only alphanumeric values allowed",
    )
    value: float = Field(
        sa_column=Column(Float()), gt=0, le=9_999_999_999, description="Product value"
    )
    description: str = Field(
        sa_column=Column(String(500)),
        description="Product description. Only alphanumeric values",
        min_length=10,
        max_length=500,
    )
    createDate: Optional[date] = Field(
        sa_column=Column(Date()), description="Creation date"
    )
    updateDate: Optional[date] = Field(
        sa_column=Column(Date()), description="Update date"
    )
    softDelete: Optional[date] = Field(
        default=None, sa_column=Column(Date()), description="SoftDelete date"
    )
