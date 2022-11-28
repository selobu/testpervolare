from pydantic import validator, BaseModel, EmailStr, Field
from tools import map_2_pydantic, digest
import re

@map_2_pydantic
class Login(BaseModel):
    email: EmailStr = Field(description="Your email")
    password: str = Field(description="Password", max_length=16, min_length=8)
    @validator('password')
    def pass_validator(cls, v):
        assert len(v) >= 8 and len(v) <= 16
        r = "".join(re.findall("[0-9]*[a-zA-Z]*[0-9]*[\*\/\+\-\$\%\&]*", v))
        assert len(r) == len(v)
        # the system only stores the sha256 for security reasons
        return digest(r)
