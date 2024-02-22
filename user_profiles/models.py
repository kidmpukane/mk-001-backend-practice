from django.db import models
from django_random_id_model import RandomIDModel
from django.contrib.auth.models import User


class BaseUser(RandomIDModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    profile_picture = models.ImageField(
        upload_to='images/', null=True, blank=True)
    background_picture = models.ImageField(
        upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Customer(BaseUser):
    at_user = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100, default="no-username")
    user_bio = models.CharField(max_length=500)
    is_merchant = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.at_user}"


class Merchant(BaseUser):
    at_merchant = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100, default="no-username")
    store_description = models.CharField(max_length=500)
    is_merchant = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.at_merchant}"
