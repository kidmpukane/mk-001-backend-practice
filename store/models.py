from django.db import models
from django_random_id_model import RandomIDModel
from user_profiles.models import Merchant


class Store(RandomIDModel):
    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=225, null=True, blank=True)
    store_description = models.CharField(max_length=225, null=True, blank=True)
    store_image = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.store_name}"
