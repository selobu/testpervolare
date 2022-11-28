from typing import Optional
from tools import map_name_to_table, digest
from sqlmodel import Field, SQLModel, Column, String, Field, Relationship
from pydantic import EmailStr, validator

import re


@map_name_to_table
class Login(SQLModel, table=True):
    email: Optional[EmailStr] = Field(default=None, primary_key=True)
    password: str = Field(sa_column=Column(String(300)), nullable=False)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates="login")

    @validator("password")
    def pass_validator(cls, v):
        assert len(v) >= 8 and len(v) <= 16
        r = "".join(re.findall("[0-9]*[a-zA-Z]*[0-9]*[\*\/\+\-\$\%\&]*", v))
        assert len(r) == len(v)
        # the system only stores the sha256 for security reasons
        return digest(r)
