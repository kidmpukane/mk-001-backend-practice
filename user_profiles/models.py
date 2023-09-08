from django.db import models


class Merchant(models.Model):

    store_name = models.CharField(max_length=225)
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    at_store = models.CharField(max_length=100)
    profile_picture = models.CharField(max_length=500)
    background_picture = models.CharField(max_length=500)
    store_description = models.CharField(max_length=500)
    date_created = models.CharField(max_length=500)
    last_updated = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.store_name}"
