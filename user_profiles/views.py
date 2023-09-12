from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Merchant
from .serializers import MerchantSerializer


@api_view(['GET'])
def get_user_data(request):
    user_data = Merchant.objects.all()
    serializer = MerchantSerializer(user_data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def register_user(request):
    serializer = MerchantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def get_user_profile(request, id):
    try:
        user_profile_data = Merchant.objects.get(pk=id)
    except Merchant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MerchantSerializer(user_profile_data)
        return Response(serializer.data)


@api_view(['PUT'])
def update_user_data(request, id):
    user_profiles_info_update = Merchant.objects.get(pk=id)
    serializer = MerchantSerializer(
        instance=user_profiles_info_update, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_user_data(request, id):
    user_profile_delete_info = Merchant.objects.get(pk=id)
    user_profile_delete_info.delete()
    return Response("User successfully deleted")
