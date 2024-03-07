from django.db.models.signals import post_save
from django.dispatch import receiver
from store.models import Store
from user_profiles.models import Customer
from .models import PrimaryCollection, SecondaryCollection, TertiaryCollection, CustomerCollection


@receiver(post_save, sender=Store)
def create_store_for_primary_collection(sender, instance, created, **kwargs):
    if created:
        # The PrimaryCollection instance is created, you can perform additional actions here
        PrimaryCollection.objects.create(
            store_id=instance, collection_title=f"{instance.store_name}'s Primary Collection", collection_image="../default_images/primary_collection.jpg")


@receiver(post_save, sender=SecondaryCollection)
def create_store_for_secondary_collection(sender, instance, created, **kwargs):
    if created:
        # The SecondaryCollection instance is created, you can perform additional actions here
        SecondaryCollection.objects.create(
            store_id=instance, collection_title=f"{instance.store_name}'s Secondary Collection", collection_image="../default_images/secondary_collection.jpg")


@receiver(post_save, sender=TertiaryCollection)
def create_store_for_tertiary_collection(sender, instance, created, **kwargs):
    if created:
        # The TertiaryCollection instance is created, you can perform additional actions here
        TertiaryCollection.objects.create(
            store_id=instance, collection_title=f"{instance.store_name}'s Tertiary Collection", collection_image="../default_images/tertiary_collection.jpg")


@receiver(post_save, sender=Customer)
def create_store_for_customer_collection(sender, instance, created, **kwargs):
    if created:
        # The CustomerCollection instance is created, you can perform additional actions here
        CustomerCollection.objects.create(
            customer_id=instance, collection_title=f"{instance.email}'s Collection", collection_image="../default_images/quarteneary_collection.jpg")
