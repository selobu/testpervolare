from pydantic import validator, BaseModel
from tools import map_2_pydantic


@map_2_pydantic
class User(BaseModel):
    id:str


