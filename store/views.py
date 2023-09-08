from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Store
from .serializers import StoreSerializer


@api_view(['GET'])
def get_store_by_id(request, id):
    try:
        store_data = Store.objects.get(pk=id)
    except Store.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StoreSerializer(store_data)
        return Response(serializer.data)
