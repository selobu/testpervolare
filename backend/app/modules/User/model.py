from typing import Optional, List
from tools import map_name_to_table
<<<<<<< HEAD
from sqlmodel import Field, SQLModel, Column, String, Field, Relationship
from pydantic import EmailStr, validator
import re
from uuid import uuid4


@map_name_to_table
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, description="UUID 4")
    nombre_completo: str = Field(
        sa_column=Column(String(400)), unique=True, description="User fullname"
    )
    cedula: str = Field(sa_column=Column(String(200)), description="your Card ID")
    departamento: str = Field(sa_column=Column(String(200)), description="Country")
    municipio: str = Field(sa_column=Column(String(200)), description="State")
    direccion: str = Field(sa_column=Column(String(250)), description="Address")
    activo: bool = True
    login: List["Login"] = Relationship(back_populates="user")
=======
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date, Integer
from sqlalchemy.orm import relationship
from pydantic import EmailStr
from config import settings

Base = settings.Base
>>>>>>> 751ea766ead9c6788c40bfd5f8f3d0e8a395bca5

    @validator("id")
    def uuid_validator(cls, v):
        if v is not None:
            res = re.findall("[0-9a-f]{12}4[0-9a-f]{3}[89ab][0-9a-f]{15}\Z", v)
            res = "".join(res)
            assert len(res) == len(v)
            return v
        else:
            return uuid4()


@map_name_to_table
<<<<<<< HEAD
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
=======
class User(Base):
    __tablename__ = "user"
    id: Mapped[Optional[int]] = mapped_column(Integer(), default=None, primary_key=True)
    nombre_completo: Mapped[str] = mapped_column(String(400), unique=True)
    cedula: Mapped[str] = mapped_column(String(200))
    departamento: Mapped[str] = mapped_column(String(200))
    municipio: Mapped[str] = mapped_column(String(200))
    direccion: Mapped[str] = mapped_column(String(250))
    activo: Mapped[bool] = True
    login: Mapped[List["Login"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
>>>>>>> 751ea766ead9c6788c40bfd5f8f3d0e8a395bca5
    )
