from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Store
from user_profiles.models import Merchant


@receiver(post_save, sender=Merchant)
def create_store_for_merchant(sender, instance, created, **kwargs):
    if created:
        # The Merchant instance is created, create a corresponding Store
        Store.objects.create(merchant_id=instance,
                             store_name=f"{instance.email}'s Store")
