from typing import Optional
from tools import map_name_to_table
from config import settings
from sqlmodel import Field, SQLModel, Column, String, Field, Date
from uuid import uuid4
from datetime import date
from pydantic import validator
import re
Tb = settings.app.Tb


@map_name_to_table
class Atributo(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True, description="UUID 4")
    name: str = Field(sa_column=Column(String(10)), description="name", max_length=10, min_length=2)
    type: str = Field(sa_column=Column(String(10)), description="Attribute type  allowed Color|Tala|Marca|Fabrica")
    createDate: date = Field(sa_column=Column(Date), description="Creation date")
    UpdateDate: date = Field(sa_column=Column(Date), descripton="Update Date")
    softDelete: Optional[date] = Field(default=None, sa_column=Column(Date), description="Softdelete date")
    @validator("id")
    def uuid_validator(cls, v):
        if v is not None:
            res = re.findall('[0-9a-f]{12}4[0-9a-f]{3}[89ab][0-9a-f]{15}\Z',v )
            res = ''.join(res)
            assert len(res) == len(v)
            return v
        else:
            return uuid4()
        
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
