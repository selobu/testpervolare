from typing import Optional, List
from tools import map_name_to_table
from sqlmodel import Field, SQLModel, Column, String, Field,\
    Relationship
from pydantic import EmailStr

@map_name_to_table
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre_completo: str = Field(sa_column=Column(String(400)), unique=True)
    cedula: str = Field(sa_column=Column(String(200)))
    departamento: str = Field(sa_column=Column(String(200)))
    municipio: str = Field(sa_column=Column(String(200)))
    direccion: str = Field(sa_column=Column(String(250)))
    activo: bool = True
    login: List["Login"] = Relationship(back_populates="user")


@map_name_to_table
class UserRegister(SQLModel):
    nombre_completo: str = Field(sa_column=Column(String(400)), unique=True)
    cedula: str = Field(sa_column=Column(String(200)))
    departamento: str = Field(sa_column=Column(String(200)))
    municipio: str = Field(sa_column=Column(String(200)))
    direccion: str = Field(sa_column=Column(String(250)))
    email: Optional[EmailStr] = Field(default=None, primary_key=True)
    password: str = Field(sa_column=Column(String(300)), nullable=False)