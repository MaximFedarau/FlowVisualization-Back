from pydantic import BaseModel, Field
from typing import List

class MenuItem(BaseModel):
    name: str
    quantity: int = Field(..., ge=1)
    price_per_unit: float = Field(..., ge=0)

class Order(BaseModel):
    customer_name: str
    table_number: int = Field(..., ge=1)
    items: List[MenuItem]
    is_takeaway: bool
