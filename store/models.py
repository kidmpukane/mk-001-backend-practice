from django.db import models
from django_random_id_model import RandomIDModel
from user_profiles.models import Merchant


class Store(RandomIDModel):
    id = models.AutoField(primary_key=True)
    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    store_name = models.CharField(
        max_length=225, null=True, blank=True, default="Enter Store Name")
    store_description = models.CharField(
        max_length=225, null=True, blank=True, default="Enter Store Description")
    store_image = models.ImageField(
        upload_to='images/', null=True, blank=True, default="../default_images/fabrice-villard-Jrl_UQcZqOc-unsplash.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.store_name}"
