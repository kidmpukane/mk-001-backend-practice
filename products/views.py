from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import (
    PrimaryProduct,
    SecondaryProduct, 
    TertiaryProduct
)
from .serializers import (
    PrimaryProductSerializer, 
    SecondaryProductSerializer, 
    TertiaryProductSerializer
)

#.......................................GET ALL USER DATA.......................................

def get_data(queryset, serializer_class):
    data = queryset.objects.all()
    serializer = serializer_class(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_primary_products(request):
    return get_data(PrimaryProduct, PrimaryProductSerializer)


@api_view(['GET'])
def get_all_secondary_products(request):
    return get_data(SecondaryProduct, SecondaryProductSerializer)


@api_view(['GET'])
def get_all_tertiary_products(request):
    return get_data(TertiaryProduct, TertiaryProductSerializer)




#.......................................REGISTER STORE.......................................

def store_registration(serializer_class, request):
    serializer = serializer_class(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_primary_product(request):
    return store_registration(PrimaryProductSerializer, request)

@api_view(['POST'])
def create_secondary_product(request):
    return store_registration(SecondaryProductSerializer, request)

@api_view(['POST'])
def create_tertiary_product(request):
    return store_registration(TertiaryProductSerializer, request)

#.......................................GET USER BY ID.......................................

def get_store(request, id, profile_model, serializer_class):
    try:
        user_profile_data = profile_model.objects.get(pk=id)
    except profile_model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = serializer_class(user_profile_data)
        return Response(serializer.data)

@api_view(['GET'])
def get_primary_product(request, id):
    return get_store(request, id, PrimaryProduct, PrimaryProductSerializer)

@api_view(['GET'])
def get_secondary_product(request, id):
    return get_store(request, id, SecondaryProduct, SecondaryProductSerializer)

@api_view(['GET'])
def get_tertiary_product(request, id):
    return get_store(request, id, TertiaryProduct, TertiaryProductSerializer)


#.......................................EDIT STORE DATA.......................................

def update_data(request, id, queryset, serializer_class):
    user_profiles_info_update = queryset.objects.get(pk=id)
    serializer = serializer_class(
        instance=user_profiles_info_update, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def edit_primary_product(request, id):
    return update_data(request, id, PrimaryProduct, PrimaryProductSerializer)

@api_view(['PUT'])
def edit_secondary_product(request, id):
    return update_data(request, id, SecondaryProduct, SecondaryProductSerializer)

@api_view(['PUT'])
def edit_tertiary_product(request, id):
    return update_data(request, id, TertiaryProduct, TertiaryProductSerializer)



#.......................................DELETE STORE DATA.......................................

def delete_collection(request, id, queryset):
    delete_store_info = queryset.objects.get(pk=id)
    delete_store_info.delete()
    return Response("This store has been successfully deleted")

@api_view(['DELETE'])
def delete_primary_product(request, id):
    return delete_collection(request, id, PrimaryProduct)

@api_view(['DELETE'])
def delete_secondary_product(request, id):
    return delete_collection(request, id, SecondaryProduct)

@api_view(['DELETE'])
def delete_tertiary_product(request, id):
    return delete_collection(request, id, TertiaryProduct)
