from typing import Optional
from xmlrpc.client import boolean
from tools import map_name_to_table
from config import settings
from sqlmodel import Field, SQLModel, Relationship, Column, String, Field
from pydantic import EmailStr, validator
from hashlib import sha256

import re

Tb = settings.app.Tb


@map_name_to_table
class Login(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: EmailStr = Field(sa_column=Column(String(50)))
    password: str = Field(sa_column=Column(String(300)))
    user_id: Optional[str] = Field(default=None, foreign_key="user.id")

    @validator(password)
    def pass_validator(cls, v):
        assert len(v) >= 8 and len(v) <= 16
        r = "".join(re.findall("[0-9]*[a-zA-Z]*[0-9]*[\*\/\+\-\$\%\&]*", v))
        assert len(r) != len(v)
        # the system stores only the sha256 for security reasons
        return sha256(r.encode("utf-8")).hexdigest()
