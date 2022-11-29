from typing import Optional, List
from tools import map_name_to_table, uuid_isvalid
from sqlmodel import Field, SQLModel, Column, String, Field, Relationship, Boolean
from pydantic import EmailStr, validator
import re
from uuid import uuid4


@map_name_to_table
class User(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True, description="UUID 4")
    nombre_completo: str = Field(
        sa_column=Column(String(400)), unique=True, description="User fullname"
    )
    cedula: str = Field(sa_column=Column(String(200)), description="your Card ID")
    departamento: str = Field(sa_column=Column(String(200)), description="Country")
    municipio: str = Field(sa_column=Column(String(200)), description="State")
    direccion: str = Field(sa_column=Column(String(250)), description="Address")
    activo: Optional[bool] = Field(default=True, sa_column=Column(Boolean))
    login: List["Login"] = Relationship(back_populates="user")

    @validator("id")
    def uuid_validator(cls, v):
        if v not in [None, "None"]:
            assert uuid_isvalid(v)
            return v
        else:
            return uuid4()


@map_name_to_table
class UserRegister(SQLModel):
    nombre_completo: str = Field(
        sa_column=Column(String(400)), unique=True, description="User fullname"
    )
    cedula: str = Field(sa_column=Column(String(200)), description="your Card ID")
    departamento: str = Field(sa_column=Column(String(200)), description="Country")
    municipio: str = Field(sa_column=Column(String(200)), description="State")
    direccion: str = Field(sa_column=Column(String(250)), description="Address")
    email: Optional[EmailStr] = Field(
        default=None, primary_key=True, description="User email"
    )
    password: str = Field(
        sa_column=Column(String(300)),
        nullable=False,
        description="User password only allowed a-z A-Z 0-9 and */+-$%&",
        max_length=12,
        min_length=8,
    )
