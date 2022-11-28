from pydantic import validator, BaseModel, EmailStr, Field
from tools import map_2_pydantic


@map_2_pydantic
class User(BaseModel):
    nombre_completo: str = Field(description='First name and last name', max_length=400, min_length=5)
    cedula: str = Field(description='Your Id Card number', max_length=200, min_length=6)
    departamento: str = Field(description='Country', max_length=200, min_length=6)
    municipio: str = Field(description='State', max_length=200, min_length=6)
    direccion: str = Field(description='Address', max_length=250, min_length=6)
    email : EmailStr = Field(description='Email address')
    password: str = Field(description='Allowed characters: 0-9, A-Z, a-z */+-$%&', max_length=16, min_length=8)
    @validator('password')
    def password_validator(cls, v):
        return v