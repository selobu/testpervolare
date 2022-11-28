from pydantic import validator, BaseModel, Field
from typing import Optional
from tools import map_2_pydantic
import re

@map_2_pydantic
class Producto(BaseModel):
    id: Optional[str]= Field(description='UUID in the format xxxxx-xxxxx-xxxx-xxxx')
    name: str = Field(description='Product name, only alphanumeric values')
    value: float = Field(description='Float values with maximum 10 digits included decimal point readed as a point',
                         min=0.01, max= 9_999_999_999)
    description: str = Field(description='Product description', max_length=500, min_length=10)
    @validator("name")
    def name_validator(cls, v):
        res = "".join(re.findall("([0-9]*[a-zA-Z]+[0-9]*)", v))
        if len(res) != len(v):
            raise ValueError("only allowed charactes and numerical values")
        return v

    @validator("value")
    def value_validator(cls, v):
        assert v > 0 and v < 9_999_999_999
        return v

    @validator("description")
    def desc_validator(cls, v):
        res = "".join(re.findall("([0-9]*[a-zA-Z]*[0-9]*)", v))
        if len(res) != len(v):
            raise ValueError("only allowed charactes and numerical values")
        return v