from django.db import models
from django_random_id_model import RandomIDModel
from accounts.models import CustomUser


class BaseUser(RandomIDModel):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, default=1)
    email = models.EmailField(null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to='images/', null=True, blank=True, default="../default_images/profile_picture.jpg")
    background_picture = models.ImageField(
        upload_to='images/', null=True, blank=True, default="../default_images/background_picture.jpg")
    user_name = models.CharField(max_length=100, default="no-username")
    user_bio = models.CharField(
        max_length=500, default="no-bio, please enter your bio :)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Customer(BaseUser):
    user_description = models.CharField(
        max_length=500, default="no-description")

    def __str__(self):
        return f"{self.email}"


class Merchant(BaseUser):
    store_description = models.CharField(
        max_length=500, default="no-description")

    def __str__(self):
        return f"{self.email}"
