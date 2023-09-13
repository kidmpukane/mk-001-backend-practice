from rest_framework import serializers
from .models import FemalePrimaryGallery, FemaleSecondaryGallery, FemaleTertiaryGallery, FemaleQuaternaryGallery, \
    MalePrimaryGallery, MaleSecondaryGallery, MaleTertiaryGallery, MaleQuaternaryGallery, \
    OtherPrimaryGallery, OtherSecondaryGallery


class FemalePrimaryGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = FemalePrimaryGallery
        fields = "__all__"


class FemaleSecondaryGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = FemaleSecondaryGallery
        fields = "__all__"


class FemaleTertiaryGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = FemaleTertiaryGallery
        fields = "__all__"


class FemaleQuaternaryGallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = FemaleQuaternaryGallery
        fields = "__all__"


class MalePrimaryGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = MalePrimaryGallery
        fields = "__all__"


class MaleSecondaryGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = MaleSecondaryGallery
        fields = "__all__"


class MaleTertiaryGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = MaleTertiaryGallery
        fields = "__all__"


class MaleQuaternaryGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = MaleQuaternaryGallery
        fields = "__all__"


class OtherPrimaryGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherPrimaryGallery
        fields = "__all__"


class OtherSecondaryGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherSecondaryGallery
        fields = "__all__"
