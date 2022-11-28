from datetime import date
from typing import Optional
from tools import map_name_to_table
from sqlmodel import Field, SQLModel, Column, String, Field, Float, Date
from uuid import uuid4
from pydantic import validator
import re


@map_name_to_table
class Producto(SQLModel, table=True):
    id: Optional[int] = Field(default=uuid4, primary_key=True)
    name: str = Field(unique=True, sa_column=Column(String(10)))
    value: float = Field(sa_column=Column(Float))
    description: str = Field(sa_column=Column(String(500)))
    createDate: date = Field(default=date.today, sa_column=Column(Date))
    updateDate: date = Field(default=None, sa_column=Column(Date))
    softDelete: Optional[date] = Field(
        default=None, sa_column=Column(Date)
    )

    @validator("name")
    def name_validator(cls, v):
        res = "".join(re.findall("([0-9]*[a-zA-Z]+[0-9]*)", v))
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
        res = "".join(re.findall("([0-9]*[a-zA-Z]+[0-9]*)", v))
        if len(res) != len(v):
            raise ValueError("only allowed charactes and numerical values")
        return v


@map_name_to_table
class ProductAttribute(SQLModel, table=True):
    product_id: str = Field(default=None, foreign_key="producto.id", primary_key=True)
    attribute_id: str = Field(default=None, foreign_key="atributo.id", primary_key=True)


@map_name_to_table
class ProductModify(SQLModel):
    name: str = Field(sa_column=Column(String(10)))
    value: float = Field(sa_column=Column(Float))
    description: str = Field(sa_column=Column(String(500)))
    softDelete: Optional[date] = Field(
        default=None, sa_column=Column(Date)
    )