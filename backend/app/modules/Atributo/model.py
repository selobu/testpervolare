from typing import Optional
from tools import map_name_to_table
from config import settings
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date
from uuid import uuid4
from datetime import date
from pydantic import validator

Tb = settings.app.Tb
Base = settings.Base

@map_name_to_table
class Atributo(Base):
    __tablename__ = 'atributo'
    id: Mapped[str] = mapped_column(default=uuid4, primary_key=True)
    name: Mapped[str] = mapped_column(String(10))
    type: Mapped[str] = mapped_column(String(10))
    createDate: Mapped[Optional[date]] = mapped_column(Date)
    UpdateDate: Mapped[Optional[date]] = mapped_column(Date)
    softDelete: Mapped[Optional[date]] = mapped_column(Date)

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
a=1