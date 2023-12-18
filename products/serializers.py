import os
import PIL
import json
import time
import pickle
import requests
import PIL.Image
import numpy as np
from PIL import Image
import tensorflow as tf
from numpy.linalg import norm
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from rest_framework import serializers
from sklearn.neighbors import NearestNeighbors
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input

from background_task import background
import logging
from .models import (
    BaseProduct,
    PrimaryProduct, 
    SecondaryProduct, 
    TertiaryProduct
)

cnn_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
class AllProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseProduct  # Use the appropriate base model
        fields = '__all__'  # Serialize all fields; adjust as needed

class ProductInputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    product_name = serializers.CharField(max_length=100)
    product_image = serializers.URLField()
    product_sizes = serializers.CharField()
    product_colours = serializers.CharField()
    feature_list = serializers.ListField(allow_null=True)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    merchant_id = serializers.IntegerField()
    collection_id = serializers.IntegerField()
class PrimaryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimaryProduct
        fields = '__all__'

    def create(self, validated_data):
        instance = PrimaryProduct(**validated_data)
        instance.save()
        enqueue_product_for_processing(instance.id, cnn_model)  # Pass the model as an argument
        return instance

class SecondaryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondaryProduct
        fields = '__all__'

    def create(self, validated_data):
        instance = SecondaryProduct(**validated_data)  # Use SecondaryProduct here
        instance.save()
        enqueue_product_for_processing(instance.id, cnn_model)  # Pass the model as an argument
        return instance

class TertiaryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TertiaryProduct
        fields = '__all__'

def enqueue_product_for_processing(product_id, model):
    # Fetch product using product_id
    try:
        primary_product = PrimaryProduct.objects.get(id=product_id)
        product = primary_product
    except PrimaryProduct.DoesNotExist:
        try:
            secondary_product = SecondaryProduct.objects.get(id=product_id)
            product = secondary_product
        except SecondaryProduct.DoesNotExist:
            # Handle the case where the product doesn't exist in either table
            return None  # Or raise an appropriate exception

    image_url = product.product_image
    image = Image.open(requests.get(image_url, stream=True).raw)
    image = image.resize((224, 224))
    image_array = np.array(image)
    image_array = np.expand_dims(image_array, axis=0)
    image_array = preprocess_input(image_array)

    # Extract features using the provided model (cnn_model)
    features = model.predict(image_array)
    flattened_features = features.flatten()
    normalized_features = flattened_features / norm(flattened_features)
    features_list = normalized_features.tolist()

    # Update the product's feature_list field
    product.feature_list = features_list
    product.save(update_fields=['feature_list', 'updated_at'])  # Save the updated field and timestamp
    return features_list