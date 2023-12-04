from django.db import models
from django_random_id_model import RandomIDModel

class BaseUser(RandomIDModel):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    profile_picture = models.CharField(max_length=500)
    background_picture = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Customer(BaseUser):
    user_name = models.CharField(max_length=225)
    at_user = models.CharField(max_length=100)
    user_bio = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.user_name}"

class Merchant(BaseUser):
    store_name = models.CharField(max_length=225)
    at_store = models.CharField(max_length=100)
    store_description = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.store_name}"
    