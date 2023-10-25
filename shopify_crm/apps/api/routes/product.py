from ninja import NinjaAPI
import queries

api = NinjaAPI()

@api.post('/insert_product')
def insert_product(request, query:queries.InsertProduct):
    return 200