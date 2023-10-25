from typing import List
from ninja import Schema


class InsertProduct(Schema):
    title: str
    body_html: str = None
    vendor: str = None
    product_type: str = None
    variants: List[str] = None
    images: List[str] = ["1", "2", "3"]
    status: str = "draft"
