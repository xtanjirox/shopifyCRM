from django.db.models.signals import post_save

from apps.core.models import Product

from django.dispatch import receiver

from apps.api.routes.product import insert_product
from apps.api.queries import InsertProduct


@receiver(post_save, sender=Product)
def call_insert_product(sender, instance, created, **kwargs):
    if created:
        q_insert_product = InsertProduct(
            id_product=instance.pk,
            title=instance.title
        )
        insert_product(request=None, product=q_insert_product)
