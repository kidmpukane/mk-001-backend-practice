from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PrimaryCollection, SecondaryCollection, TertiaryCollection
from .serializers import PrimaryCollectionSerializer, SecondaryCollectionSerializer, TertiaryCollectionSerializer


@api_view(['GET'])
def get_primary_collection(request, store_id):
    try:
        primary_collection_query = PrimaryCollection.objects.get(
            store_id=store_id)
    except PrimaryCollection.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PrimaryCollectionSerializer(primary_collection_query)
        return Response(serializer.data)


@api_view(['GET'])
def get_secondary_collection(request, store_id):
    try:
        secondary_collection_query = SecondaryCollection.objects.get(
            store_id=store_id)
    except SecondaryCollection.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SecondaryCollectionSerializer(secondary_collection_query)
        return Response(serializer.data)


@api_view(['GET'])
def get_tertiary_collection(request, store_id):
    try:
        tertiary_collection_query = TertiaryCollection.objects.get(
            store_id=store_id)
    except TertiaryCollection.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TertiaryCollectionSerializer(tertiary_collection_query)
        return Response(serializer.data)
