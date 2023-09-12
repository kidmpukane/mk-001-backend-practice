from django.db import models
from user_profiles.models import Merchant
from django_random_id_model import RandomIDModel


class Store(RandomIDModel):

    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=300)
    store_description = models.CharField(max_length=300)
    store_cover_image = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.store_name}"
