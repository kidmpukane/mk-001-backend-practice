from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PrimaryProduct
from .serializers import PrimaryProductSerializer


@api_view(['GET'])
def get_primary_product(request, store_gallery_id):
    try:

        primary_product_query = PrimaryProduct.objects.filter(
            store_gallery_id=store_gallery_id)
    except PrimaryProduct.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PrimaryProductSerializer(
            primary_product_query, many=True)
        return Response(serializer.data)
