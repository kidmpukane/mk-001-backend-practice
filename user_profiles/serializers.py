from rest_framework import serializers
from .models import Merchant, Customer

class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
