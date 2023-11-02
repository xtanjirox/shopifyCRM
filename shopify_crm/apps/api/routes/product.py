from apps.api import queries
from ninja import Router
from ninja_extra import NinjaExtraAPI
import requests
import json
from apps.core import models

api = NinjaExtraAPI()
router = Router()


@router.post('/insert_product')
def insert_product(request, product: queries.InsertProduct):
    url = "https://reeza01.myshopify.com/admin/api/2023-07/products.json"
    var = {
        "title": product.title,
        "body_html": product.body_html,
        "vendor": product.vendor,
        "product_type": product.product_type,
        "status": models.ProductStatus.choices[product.status][1],
        "variants": product.variants,
        "images": product.images
    }
    payload = json.dumps({
        "product": var
    })
    headers = {
        'Content-Type': 'application/json',
        'X-Shopify-Access-Token': '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'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 201:
        models.Product.objects.filter(pk=product.id_product).update(publish_status=True)
    else:
        print(f'error :{response.text}')
    return 200
