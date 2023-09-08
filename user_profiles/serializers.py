from rest_framework import serializers
from .models import Merchant

class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = ['id', 'store_name', 'first_name', 'last_name', 'at_store', 'profile_picture', 'background_picture', 'store_description', 'date_created', 'last_updated']
