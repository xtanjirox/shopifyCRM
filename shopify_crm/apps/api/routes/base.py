from .product import router as product_router
from ninja import NinjaAPI
from ninja_extra import NinjaExtraAPI
from django.urls import path
from django.contrib import admin


api = NinjaExtraAPI()

api.add_router("/", product_router)

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/", api.urls),
]