from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Merchant, Customer
from .serializers import MerchantSerializer, CustomerSerializer


#.......................................GET ALL USER DATA.......................................

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





#.......................................REGISTER USERS.......................................

def register_user(serializer_class):
    serializer = serializer_class(data=request.data)
    if serializer.is_valid():
        serializer.save()


@api_view(['POST'])
def register_merchant(request):
    return register_user(MerchantSerializer)


@api_view(['POST'])
def register_customer(request):
    return register_user(CustomerSerializer)




#.......................................GET USER BY ID.......................................

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



#.......................................EDIT USER DATA.......................................

# @api_view(['PUT'])
# def update_user_data(request, id):
#     user_profiles_info_update = Merchant.objects.get(pk=id)
#     serializer = MerchantSerializer(
#         instance=user_profiles_info_update, data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# @api_view(['DELETE'])
# def delete_user_data(request, id):
#     user_profile_delete_info = Merchant.objects.get(pk=id)
#     user_profile_delete_info.delete()
#     return Response("User successfully deleted")
