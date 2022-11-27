from typing import Optional
from xmlrpc.client import boolean
from tools import map_name_to_table
from config import settings
from sqlmodel import Field, SQLModel, Relationship, Column, String, Field
from pydantic import EmailStr

Tb = settings.app.Tb


@map_name_to_table
class Login(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: EmailStr = Field(sa_column=Column(String(16)))
    password: str = Field(sa_column=Column(String(16)))