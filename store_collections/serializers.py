from rest_framework import serializers
from .models import (
    PrimaryCollection, 
    SecondaryCollection, 
    TertiaryCollection, 
    CustomerCollection
)


class PrimaryCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimaryCollection
        fields = '__all__'

class SecondaryCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondaryCollection
        fields = '__all__'

class TertiaryCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TertiaryCollection
        fields = '__all__'

class CustomerCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCollection
        fields = '__all__'