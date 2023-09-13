from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from store_galleries.models import FemalePrimaryGallery, FemaleSecondaryGallery, FemaleTertiaryGallery, FemaleQuaternaryGallery
from user_profiles.models import Merchant


class PrimaryProduct(models.Model):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    store_gallery_id = GenericForeignKey('content_type', 'object_id')

    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=250)
    product_description = models.CharField(max_length=250)
    product_sizes = models.CharField(max_length=250)
    product_colours = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product_name}"
