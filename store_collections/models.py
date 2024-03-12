from django.db import models
from django_random_id_model import RandomIDModel
from store.models import Store
from user_profiles.models import Customer


class BaseCollection(RandomIDModel):
    id = models.AutoField(primary_key=True)
    collection_title = models.CharField(
        max_length=150, null=True, blank=True, default="Collection Title")
    collection_subtitle = models.CharField(
        max_length=100, null=True, blank=True, default="Collection Subtitle")
    collection_image = models.ImageField(
        upload_to='images/', null=True, blank=True, default="../default_images/profile_picture.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PrimaryCollection(BaseCollection):
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.collection_title}"


class SecondaryCollection(BaseCollection):
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.collection_title}"


class TertiaryCollection(BaseCollection):
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.collection_title}"


class CustomerCollection(BaseCollection):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.collection_title}"
