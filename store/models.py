from django.db import models
from django_random_id_model import RandomIDModel
from user_profiles.models import Merchant

class Store(RandomIDModel):
    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=225)
    store_description = models.CharField(max_length=225)
    store_image = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.store_name}"