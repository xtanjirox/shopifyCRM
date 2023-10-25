from apps.api import queries
from ninja import Router
from ninja_extra import NinjaExtraAPI
import requests
import json

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
            "status": product.status,
            "variants": product.variants,
            "images": product.images
        }
    print(var)
    payload = json.dumps({
        "product": var
    })
    headers = {
        'Content-Type': 'application/json',
        'X-Shopify-Access-Token': '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'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        print(f'success: {response.text}')
    else:
        print(f'error :{response.text}')
    print(response.content)
    return 200
