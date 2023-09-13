from django.db import models
from store_collections.models import PrimaryCollection, SecondaryCollection, TertiaryCollection


class FemalePrimaryGallery(models.Model):

    primary_collection_id = models.ForeignKey(
        PrimaryCollection, on_delete=models.CASCADE)
    gallery_title = models.CharField(max_length=300)
    gallery_subtitle = models.CharField(max_length=300)
    gallery_image = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.gallery_title}"


class FemaleSecondaryGallery(models.Model):

    primary_collection_id = models.ForeignKey(
        PrimaryCollection, on_delete=models.CASCADE)
    gallery_title = models.CharField(max_length=300)
    gallery_subtitle = models.CharField(max_length=300)
    gallery_image = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.gallery_title}"


class FemaleTertiaryGallery(models.Model):

    primary_collection_id = models.ForeignKey(
        PrimaryCollection, on_delete=models.CASCADE)
    gallery_title = models.CharField(max_length=300)
    gallery_subtitle = models.CharField(max_length=300)
    gallery_image = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.gallery_title}"


class FemaleQuaternaryGallery(models.Model):

    primary_collection_id = models.ForeignKey(
        PrimaryCollection, on_delete=models.CASCADE)
    gallery_title = models.CharField(max_length=300)
    gallery_subtitle = models.CharField(max_length=300)
    gallery_image = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.gallery_title}"


class MalePrimaryGallery(models.Model):

    secondary_collection_id = models.ForeignKey(
        SecondaryCollection, on_delete=models.CASCADE)
    gallery_title = models.CharField(max_length=300)
    gallery_subtitle = models.CharField(max_length=300)
    gallery_image = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.gallery_title}"


class MaleSecondaryGallery(models.Model):

    secondary_collection_id = models.ForeignKey(
        SecondaryCollection, on_delete=models.CASCADE)
    gallery_title = models.CharField(max_length=300)
    gallery_subtitle = models.CharField(max_length=300)
    gallery_image = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.gallery_title}"


class MaleTertiaryGallery(models.Model):

    secondary_collection_id = models.ForeignKey(
        SecondaryCollection, on_delete=models.CASCADE)
    gallery_title = models.CharField(max_length=300)
    gallery_subtitle = models.CharField(max_length=300)
    gallery_image = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.gallery_title}"


class MaleQuaternaryGallery(models.Model):

    secondary_collection_id = models.ForeignKey(
        SecondaryCollection, on_delete=models.CASCADE)
    gallery_title = models.CharField(max_length=300)
    gallery_subtitle = models.CharField(max_length=300)
    gallery_image = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.gallery_title}"


class OtherPrimaryGallery(models.Model):

    tertiary_collection_id = models.ForeignKey(
        TertiaryCollection, on_delete=models.CASCADE)
    gallery_title = models.CharField(max_length=300)
    gallery_subtitle = models.CharField(max_length=300)
    gallery_image = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.gallery_title}"


class OtherSecondaryGallery(models.Model):

    tertiary_collection_id = models.ForeignKey(
        TertiaryCollection, on_delete=models.CASCADE)
    gallery_title = models.CharField(max_length=300)
    gallery_subtitle = models.CharField(max_length=300)
    gallery_image = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.gallery_title}"
