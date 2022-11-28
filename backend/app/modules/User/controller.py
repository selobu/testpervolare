from pydantic import validator, BaseModel, EmailStr
from tools import map_2_pydantic


@map_2_pydantic
class User(BaseModel):
    nombre_completo: str
    cedula: str
    departamento: str
    municipio: str
    direccion: str
    activo: bool
    email : EmailStr
    password: str


