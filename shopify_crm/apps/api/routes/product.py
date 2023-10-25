from ninja import Router, UploadedFile
from apps.api import queries
from ninja_extra import NinjaExtraAPI

api = NinjaExtraAPI()
router = Router()


@router.post('/insert_product')
def insert_product(request, query:queries.InsertProduct):
    return query