from django.db import models
from datetime import datetime


class ProductStatus(models.IntegerChoices):
    DRAFT = 0, 'draft'
    ACTIVE = 1, 'active'
    ARCHIVED = 2, 'archived'


class PublishedScope(models.IntegerChoices):
    GLOBAL = 0, "global"
    WEB = 1, "web"


class ProductImage(models.Model):
    image_link = models.CharField(max_length=150)


class Product(models.Model):
    title = models.CharField(max_length=150)
    status = models.IntegerField(choices=ProductStatus, blank=True)
    body_html = models.CharField(max_length=150, blank=True)
    handle = models.CharField(max_length=150, blank=True)
    image = models.ManyToManyField(ProductImage)
    options = models.CharField(max_length=150, blank=True)
    product_type = models.CharField(max_length=150, blank=True)
    published_scope = models.IntegerField(choices=PublishedScope, blank=True)
    tags = models.CharField(max_length=150, blank=True)
    template_suffix = models.CharField(max_length=150, blank=True)
    product_variants = models.CharField(max_length=150, blank=True)
    vendor = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(default=datetime.now())
    published_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())
