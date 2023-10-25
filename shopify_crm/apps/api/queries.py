from ninja import Schema
from typing import List


class InsertProduct(Schema):
    product_name: str
    product_price: float
    product_image: List[str] = None
