from django.contrib import admin
from . import models


admin.site.register(models.OptionProduct)
admin.site.register(models.ProductImage)
admin.site.register(models.Product)
admin.site.register(models.ProductVariant)
admin.site.register(models.PresentmentPrice)
