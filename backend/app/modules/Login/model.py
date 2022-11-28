from typing import Optional
from tools import map_name_to_table, digest
<<<<<<< HEAD
<<<<<<< HEAD
from sqlmodel import Field, SQLModel, Column, String, Field, Relationship
=======
=======
>>>>>>> 751ea766ead9c6788c40bfd5f8f3d0e8a395bca5
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String, Date
from sqlalchemy import ForeignKey

from config import settings

# from sqlmodel import Field, SQLModel, Column, String, Field, Relationship
<<<<<<< HEAD
>>>>>>> b56f21e (black apply)
=======
>>>>>>> 751ea766ead9c6788c40bfd5f8f3d0e8a395bca5
from pydantic import EmailStr, validator

import re

Base = settings.Base



@map_name_to_table
<<<<<<< HEAD
<<<<<<< HEAD
class Login(SQLModel, table=True):
    email: Optional[EmailStr] = Field(
        default=None, primary_key=True, description="Use email"
    )
    password: str = Field(
        sa_column=Column(String(300)),
        nullable=False,
        description="User password only allowed a-z A-Z 0-9 and */+-$%&",
    )
    user_id: Optional[int] = Field(
        default=None, foreign_key="user.id", description="user id"
    )
    user: Optional["User"] = Relationship(back_populates="login")

    @validator("password")
    def pass_validator(cls, v):
        assert len(v) >= 8 and len(v) <= 16
        r = "".join(re.findall("[0-9]*[a-zA-Z]*[0-9]*[\*\/\+\-\$\%\&]*", v))
        assert len(r) == len(v)
        # the system only stores the sha256 for security reasons
        return digest(r)
=======
class Login(Base):
    __tablename__ = "login"
    email: Mapped[Optional[EmailStr]] = mapped_column(String(200), primary_key=True)
    password: Mapped[str] = mapped_column(String(300), nullable=False)
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("user.id"))

    user: Mapped["User"] = relationship(back_populates="login")
>>>>>>> b56f21e (black apply)
=======
class Login(Base):
    __tablename__ = "login"
    email: Mapped[Optional[EmailStr]] = mapped_column(String(200), primary_key=True)
    password: Mapped[str] = mapped_column(String(300), nullable=False)
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("user.id"))

    user: Mapped["User"] = relationship(back_populates="login")
>>>>>>> 751ea766ead9c6788c40bfd5f8f3d0e8a395bca5
