from rest_framework import serializers
from background_task import background
import logging
from .models import (
    PrimaryProduct, 
    SecondaryProduct, 
    TertiaryProduct
)

logger = logging.getLogger(__name__) 

class PrimaryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimaryProduct
        fields = '__all__'

    def create(self, validated_data):
        instance = PrimaryProduct(**validated_data)
        instance.save()
        enqueue_product_for_processing(instance.id)  # Enqueue product for feature extraction
        return instance

class SecondaryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondaryProduct
        fields = '__all__'

    def create(self, validated_data):
        instance = PrimaryProduct(**validated_data)
        instance.save()
        enqueue_product_for_processing(instance.id)  # Enqueue product for feature extraction
        return instance

class TertiaryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TertiaryProduct
        fields = '__all__'

def enqueue_product_for_processing(product_id):
     print("Enqueueing....")