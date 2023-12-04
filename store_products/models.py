from django.db import models
from store_galleries.models import (
    FemalePrimaryGallery,
    FemaleSecondaryGallery,
    FemaleTertiaryGallery,
    FemaleQuaternaryGallery
)
from user_profiles.models import Merchant


class BaseProduct(models.Model):
    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=250)
    product_image = models.CharField(max_length=250)
    product_sizes = models.CharField(max_length=250)
    product_colours = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PrimaryProduct(BaseProduct):
    gallery_id = models.ForeignKey(FemalePrimaryGallery, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_name}"


class SecondaryProduct(BaseProduct):
    gallery_id = models.ForeignKey(FemaleSecondaryGallery, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_name}"


class TertiaryProduct(BaseProduct):
    gallery_id = models.ForeignKey(FemaleTertiaryGallery, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_name}"


class QuaternaryProduct(BaseProduct):
    gallery_id = models.ForeignKey(FemaleQuaternaryGallery, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_name}"
