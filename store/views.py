from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Store
from .serializers import StoreSerializer


@api_view(['GET'])
def get_store_by_id(request, merchant_id):
    try:

        store_query = Store.objects.filter(merchant_id=merchant_id)
    except Store.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StoreSerializer(store_query, many=True)
        return Response(serializer.data)
