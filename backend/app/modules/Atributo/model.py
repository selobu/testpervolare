from typing import Optional
from tools import map_name_to_table
from config import settings
from sqlmodel import Field, SQLModel, Column, String,\
    Field, Date
from uuid import uuid4
from datetime import date
Tb = settings.app.Tb


@map_name_to_table
class Atributo(SQLModel, table=True):
    id: Optional[int] = Field(default=uuid4, primary_key=True)
    name: str = Field(sa_column=Column(String(10)))
    type: str = Field(sa_column=Column(String(10)))
    createDate: date = Field(sa_column=Column(Date))
    UpdateDate: date = Field(sa_column=Column(Date))
    softDelete: Optional[date] = Field(default=None, sa_column=Column(Date))