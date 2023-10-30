from django.db import models
from datetime import datetime


class ProductStatus(models.IntegerChoices):
    DRAFT = 0, 'draft'
    ACTIVE = 1, 'active'
    ARCHIVED = 2, 'archived'


class PublishedScope(models.IntegerChoices):
    GLOBAL = 0, "global"
    WEB = 1, "web"


class InventoryPolicy(models.IntegerChoices):
    DENY = 0, 'deny'


class Price(models.Model):
    currency_code = models.CharField(max_length=15)
    amount = models.CharField(max_length=30)

    class Meta:
        db_table = 'price'


class OptionProduct(models.Model):
    option1 = models.CharField(max_length=30)

    class Meta:
        db_table = 'option_product'


class ProductImage(models.Model):
    image_link = models.CharField(max_length=150)

    class Meta:
        db_table = 'product_image_shopify'


class Product(models.Model):
    title = models.CharField(max_length=150)
    status = models.IntegerField(choices=ProductStatus.choices, blank=True, null=True)
    body_html = models.CharField(max_length=150, blank=True, null=True)
    handle = models.CharField(max_length=150, blank=True, null=True)
    image = models.ManyToManyField(ProductImage)
    options = models.CharField(max_length=150, blank=True, null=True)
    product_type = models.CharField(max_length=150, blank=True, null=True)
    published_scope = models.IntegerField(choices=PublishedScope.choices, blank=True, null=True)
    tags = models.CharField(max_length=150, blank=True, null=True)
    template_suffix = models.CharField(max_length=150, blank=True, null=True)
    product_variants = models.CharField(max_length=150, blank=True, null=True)
    vendor = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now())
    published_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'product'


class ProductVariant(models.Model):
    barcode = models.CharField(max_length=150)
    compare_at_price = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now())
    fulfillment_service = models.CharField(max_length=150, blank=True, null=True)
    grams = models.IntegerField(blank=True)
    image = models.ForeignKey(ProductImage, on_delete=models.DO_NOTHING)
    inventory_item = models.IntegerField(default=0)
    inventory_management = models.CharField(max_length=150, blank=True, null=True)
    inventory_policy = models.IntegerField(choices=InventoryPolicy.choices, blank=True, null=True)
    inventory_quantity = models.IntegerField(default=0, blank=True, null=True)
    option = models.ForeignKey(OptionProduct, on_delete=models.DO_NOTHING, blank=True, null=True)
    position = models.IntegerField(default=0, blank=True, null=True)
    price = models.CharField(max_length=150, blank=True, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    sku = models.CharField(max_length=150, blank=True, null=True)
    taxable = models.BooleanField(blank=True)
    tax_code = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=150)
    updated_at = models.DateTimeField(default=datetime.now())
    weight = models.IntegerField(default=0, blank=True, null=True)
    weight_unit = models.CharField(max_length=150)

    class Meta:
        db_table = 'product_variant'


class PresentmentPrice(models.Model):
    price = models.ForeignKey(Price, on_delete=models.CASCADE, related_name='pprice')
    compare_at_price = models.ForeignKey(Price, on_delete=models.CASCADE, related_name='cpprice')
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)

    class Meta:
        db_table = 'presentment_price'
