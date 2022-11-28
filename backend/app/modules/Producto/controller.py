from pydantic import validator, BaseModel
from tools import map_2_pydantic
import re

@map_2_pydantic
class Producto(BaseModel):
    name: str
    value: int
    description: str
    @validator("name")
    def name_validator(cls, v):
        res = "".join(re.findall("([0-9]*[a-zA-Z]+[0-9]*)", v))
        if len(res) != len(v):
            raise ValueError("only allowed charactes and numerical values")
        return v

    @validator("value")
    def value_validator(cls, v):
        assert v > 0
        return v

    @validator("description")
    def desc_validator(cls, v):
        assert len(v) >= 10 and len(v) <= 500
        res = "".join(re.findall("([0-9]*[a-zA-Z]+[0-9]*)", v))
        if len(res) != len(v):
            raise ValueError("only allowed charactes and numerical values")
        return v