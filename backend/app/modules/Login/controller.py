from pydantic import validator, BaseModel, EmailStr, Field
from tools import map_2_pydantic


@map_2_pydantic
class Login(BaseModel):
    email: EmailStr = Field(description="Your email")
    password: str = Field(description="Password", max_length=16, min_length=8)
