from typing import Optional
from tools import map_name_to_table
from config import settings
from sqlmodel import Field, SQLModel, Column, String, Field, Date
from uuid import uuid4
from datetime import date
from pydantic import validator

Tb = settings.app.Tb


@map_name_to_table
class Atributo(SQLModel, table=True):
    id: Optional[int] = Field(default=uuid4, primary_key=True)
    name: str = Field(sa_column=Column(String(10)))
    type: str = Field(sa_column=Column(String(10)))
    createDate: date = Field(sa_column=Column(Date))
    UpdateDate: date = Field(sa_column=Column(Date))
    softDelete: Optional[date] = Field(default=None, sa_column=Column(Date))
    
    @validator("name")
    def name_validator(cls, v):
        if not (len(v) >= 2 and len(v) <= 10):
            raise ValueError("name len incorrect, only allowed >> 10 > name > 2,")
        return v

    @validator("type")
    def type_validator(cls, v):
        allowed = ["Color", "Talla", "Marca", "Fábrica"]
        if v not in allowed:
            raise ValueError(f"type incorrect, only allowed {allowed}")
        return v
