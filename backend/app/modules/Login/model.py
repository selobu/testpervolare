from typing import Optional
from tools import map_name_to_table, digest
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String, Date
from sqlalchemy import ForeignKey

from config import settings
#from sqlmodel import Field, SQLModel, Column, String, Field, Relationship
from pydantic import EmailStr, validator

import re

Base = settings.Base

@map_name_to_table
class Login(Base):
    __tablename__ ='login'
    email: Mapped[Optional[EmailStr]] = mapped_column(String(200), primary_key=True)
    password: Mapped[str] = mapped_column(String(300),nullable=False)
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("user.id"))
    
    user: Mapped["User"] = relationship(back_populates="login")
