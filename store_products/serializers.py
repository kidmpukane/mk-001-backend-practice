from .models import PrimaryProduct
from rest_framework import serializers


class PrimaryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimaryProduct
        fields = '__all__'
