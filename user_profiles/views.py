from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Merchant, Customer
from .serializers import MerchantSerializer, CustomerSerializer


# .......................................GET ALL USER DATA.......................................

def get_data(queryset, serializer_class):
    data = queryset.objects.all()
    serializer = serializer_class(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_merchant_data(request):
    return get_data(Merchant, MerchantSerializer)


@api_view(['GET'])
def get_all_customer_data(request):
    return get_data(Customer, CustomerSerializer)


# .......................................REGISTER USERS.......................................

def register_user(serializer_class, request):
    serializer = serializer_class(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register_merchant(request):
    return register_user(MerchantSerializer, request)


@api_view(['POST'])
def register_customer(request):
    return register_user(CustomerSerializer, request)


# .......................................GET USER BY ID.......................................

def get_profile(request, id, profile_model, serializer_class):
    try:
        user_profile_data = profile_model.objects.get(pk=id)
    except profile_model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializer_class(user_profile_data)
        return Response(serializer.data)


@api_view(['GET'])
def get_customer_profile(request, id):
    return get_profile(request, id, Customer, CustomerSerializer)


@api_view(['GET'])
def get_merchant_profile(request, id):
    return get_profile(request, id, Merchant, MerchantSerializer)


# .......................................EDIT USER DATA.......................................

@api_view(['PUT'])
def update_user_data(request, id, model_class, serializer_class):
    instance = model_class.objects.get(pk=id)
    serializer = serializer_class(instance=instance, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def update_merchant_data(request, id):
    return update_user_data(request, id, Merchant, MerchantSerializer)


@api_view(['PUT'])
def update_customer_data(request, id):
    return update_user_data(request, id, Customer, CustomerSerializer)


@api_view(['DELETE'])
def delete_user_data(request, id):
    user_profile_delete_info = Customer.objects.get(pk=id)
    user_profile_delete_info.delete()
    return Response("User successfully deleted")


class UpdateUserData(APIView):
    def put(self, request, id, model_class, serializer_class):
        instance = get_object_or_404(model_class, pk=id)
        serializer = serializer_class(instance=instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateCustomerData(UpdateUserData):
    def put(self, request, id):
        return super().put(request, id, Customer, CustomerSerializer)


class UpdateMerchantData(UpdateUserData):
    def put(self, request, id):
        return super().put(request, id, Merchant, MerchantSerializer)
