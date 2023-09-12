from django.db import models
from django_random_id_model import RandomIDModel


class Merchant(RandomIDModel):

    store_name = models.CharField(max_length=225)
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    at_store = models.CharField(max_length=100)
    profile_picture = models.CharField(max_length=500)
    background_picture = models.CharField(max_length=500)
    store_description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.store_name}"
