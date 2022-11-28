from pydantic import validator, BaseModel, Field
from tools import map_2_pydantic
from typing import Optional
from datetime import date


@map_2_pydantic
class Atributo(BaseModel):
    id: Optional[str] = Field(description="Attribute id, uuid 4 format allowed i.e.")
    name: str = Field(description="Product Name")
    type: str = Field(
        description="Product Attribute",
        unique_items=["Color", "Talla", "Fábrica", "Marca"],
    )
    softDelete: date = Field(description="Attritute softDelete date")
