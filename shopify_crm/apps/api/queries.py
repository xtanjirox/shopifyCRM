from typing import List
from ninja import Schema


class InsertProduct(Schema):
    id_product: int
    title: str
    status: int = 1
    body_html: str = None
    vendor: str = None
    product_type: str = None
    variants: List[str] = None
    images: List[str] = None
    published_scope: int = None
    handle: str = None
    options: str = None
    tags: str = None
    template_suffix: str = None
