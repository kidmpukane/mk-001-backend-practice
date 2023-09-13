from django.db import models
from store.models import Store


class PrimaryCollection(models.Model):

    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    collection_title = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.collection_title}"


class SecondaryCollection(models.Model):

    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    collection_title = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.collection_title}"


class TertiaryCollection(models.Model):

    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    collection_title = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.collection_title}"
