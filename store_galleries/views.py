from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FemalePrimaryGallery, FemaleSecondaryGallery, FemaleTertiaryGallery, FemaleQuaternaryGallery, \
    MalePrimaryGallery, MaleSecondaryGallery, MaleTertiaryGallery, MaleQuaternaryGallery, \
    OtherPrimaryGallery, OtherSecondaryGallery
from .serializer import FemalePrimaryGallerySerializer, FemaleSecondaryGallerySerializer, FemaleTertiaryGallerySerializer, FemaleQuaternaryGallerySerializers, \
    MalePrimaryGallerySerializer, MaleSecondaryGallerySerializer, MaleTertiaryGallerySerializer, MaleQuaternaryGallerySerializer, \
    OtherPrimaryGallerySerializer, OtherSecondaryGallerySerializer


@api_view(['GET'])
def get_female_primary_gallery(request, primary_collection_id):
    try:

        female_primary_gallery_query = FemalePrimaryGallery.objects.filter(
            primary_collection_id=primary_collection_id)
    except FemalePrimaryGallery.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = FemalePrimaryGallerySerializer(
            female_primary_gallery_query, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_female_secondary_gallery(request, primary_collection_id):
    try:

        female_secondary_gallery_query = FemaleSecondaryGallery.objects.filter(
            primary_collection_id=primary_collection_id)
    except FemaleSecondaryGallery.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = FemaleSecondaryGallerySerializer(
            female_secondary_gallery_query, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_female_tertiary_gallery(request, primary_collection_id):
    try:

        female_tertiary_gallery_query = FemaleTertiaryGallery.objects.filter(
            primary_collection_id=primary_collection_id)
    except FemaleTertiaryGallery.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = FemaleTertiaryGallerySerializer(
            female_tertiary_gallery_query, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_female_quaternary_gallery(request, primary_collection_id):
    try:

        female_quaternary_gallery_query = FemaleQuaternaryGallery.objects.filter(
            primary_collection_id=primary_collection_id)
    except FemaleQuaternaryGallery.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = FemaleQuaternaryGallerySerializers(
            female_quaternary_gallery_query, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_male_primary_gallery(request, secondary_collection_id):
    try:

        male_primary_gallery_query = MalePrimaryGallery.objects.filter(
            secondary_collection_id=secondary_collection_id)
    except MalePrimaryGallery.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MalePrimaryGallerySerializer(
            male_primary_gallery_query, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_male_secondary_gallery(request, secondary_collection_id):
    try:

        male_secondary_gallery_query = MaleSecondaryGallery.objects.filter(
            secondary_collection_id=secondary_collection_id)
    except MaleSecondaryGallery.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MaleSecondaryGallerySerializer(
            male_secondary_gallery_query, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_male_tertiary_gallery(request, secondary_collection_id):
    try:

        male_tertiary_gallery_query = MaleTertiaryGallery.objects.filter(
            secondary_collection_id=secondary_collection_id)
    except MaleTertiaryGallery.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MaleTertiaryGallerySerializer(
            male_tertiary_gallery_query, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_male_quaternary_gallery(request, secondary_collection_id):
    try:

        male_quaternary_gallery_query = MaleQuaternaryGallery.objects.filter(
            secondary_collection_id=secondary_collection_id)
    except MaleQuaternaryGallery.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MaleQuaternaryGallerySerializer(
            male_quaternary_gallery_query, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_other_primary_gallery(request, tertiary_collection_id):
    try:

        other_primary_gallery_query = OtherPrimaryGallery.objects.filter(
            tertiary_collection_id=tertiary_collection_id)
    except OtherPrimaryGallery.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = OtherPrimaryGallerySerializer(
            other_primary_gallery_query, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_other_secondary_gallery(request, tertiary_collection_id):
    try:

        other_secondary_gallery_query = OtherSecondaryGallery.objects.filter(
            tertiary_collection_id=tertiary_collection_id)
    except OtherSecondaryGallery.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = OtherSecondaryGallerySerializer(
            other_secondary_gallery_query, many=True)
        return Response(serializer.data)
