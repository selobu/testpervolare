from typing import Optional, List
from tools import map_name_to_table
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date, Integer
from sqlalchemy.orm import relationship
from pydantic import EmailStr
from config import settings

Base = settings.Base


@map_name_to_table
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
    )
