from rest_framework import serializers
from .models import (
    PrimaryProduct, 
    SecondaryProduct, 
    TertiaryProduct
)

class PrimaryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimaryProduct
        fields = '__all__'

class SecondaryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondaryProduct
        fields = '__all__'

class TertiaryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TertiaryProduct
        fields = '__all__'
