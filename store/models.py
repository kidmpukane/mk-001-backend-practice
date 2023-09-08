from django.db import models
from user_profiles.models import Merchant


class Store(models.Model):

    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=300)
    store_description = models.CharField(max_length=300)
    store_cover_image = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.store_name}"
