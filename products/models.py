from django.db import models
from store_collections.models import (
    PrimaryCollection,
    SecondaryCollection,
    TertiaryCollection,
)
from user_profiles.models import Merchant


class BaseProduct(models.Model):
    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=250)
    product_image = models.ImageField(
        upload_to='images/', null=True, blank=True, default="../default_images/fabrice-villard-Jrl_UQcZqOc-unsplash.jpg")
    product_sizes = models.CharField(max_length=250)
    product_colours = models.CharField(max_length=250)
    feature_list = models.JSONField(default=list, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PrimaryProduct(BaseProduct):
    collection_id = models.ForeignKey(
        PrimaryCollection, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_name}"


class SecondaryProduct(BaseProduct):
    collection_id = models.ForeignKey(
        SecondaryCollection, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_name}"


class TertiaryProduct(BaseProduct):
    collection_id = models.ForeignKey(
        TertiaryCollection, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_name}"
