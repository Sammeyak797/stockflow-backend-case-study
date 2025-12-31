from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    sku: str
    price: float
    low_stock_threshold: Optional[int] = 10


class InventoryUpdate(BaseModel):
    product_id: int
    warehouse_id: int
    quantity: int
