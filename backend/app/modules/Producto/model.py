from datetime import date
from typing import Optional
from xmlrpc.client import boolean
from tools import map_name_to_table
from sqlmodel import Field, SQLModel, Relationship, Column, String,\
    Field, Float, Date
from pydantic import EmailStr
from uuid import uuid4

@map_name_to_table
class Producto(SQLModel, table=True):
    id: Optional[int] = Field(default=uuid4, primary_key=True)
    name: str = Field(unique=True, sa_column=Column(String(10)))
    value: float = Field(sa_column=Column(Float))
    description: str = Field(sa_column=Column(String(500)))
    createDate: date = Field(sa_column=Column(Date))
    updateDate: date = Field(sa_column=Column(Date))
    softDelete: Optional[date] = Field(default = None, sa_column=Column(Date))