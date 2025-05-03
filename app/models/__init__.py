from pydantic import BaseModel, Field


class MenuItem(BaseModel):
    """MenuItem class."""

    name: str
    quantity: int = Field(..., ge=1)
    price_per_unit: float = Field(..., ge=0)


class Order(BaseModel):
    """Order class."""

    customer_name: str
    table_number: int = Field(..., ge=1)
    items: list[MenuItem]
    is_takeaway: bool
