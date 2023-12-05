from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import (
    PrimaryCollection, 
    SecondaryCollection, 
    TertiaryCollection, 
    CustomerCollection
)
from .serializers import (
    PrimaryCollectionSerializer, 
    SecondaryCollectionSerializer, 
    TertiaryCollectionSerializer, 
    CustomerCollectionSerializer
)

#.......................................GET ALL USER DATA.......................................

def get_data(queryset, serializer_class):
    data = queryset.objects.all()
    serializer = serializer_class(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_primary_collections(request):
    return get_data(PrimaryCollection, PrimaryCollectionSerializer)


@api_view(['GET'])
def get_all_secondary_collections(request):
    return get_data(SecondaryCollection, SecondaryCollectionSerializer)


@api_view(['GET'])
def get_all_tertiary_collections(request):
    return get_data(TertiaryCollection, TertiaryCollectionSerializer)


@api_view(['GET'])
def get_all_customer_collections(request):
    return get_data(CustomerCollection, CustomerCollectionSerializer)



#.......................................REGISTER STORE.......................................

def store_registration(serializer_class, request):
    serializer = serializer_class(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_primary_collection(request):
    return store_registration(PrimaryCollectionSerializer, request)

@api_view(['POST'])
def create_secondary_collection(request):
    return store_registration(SecondaryCollectionSerializer, request)

@api_view(['POST'])
def create_tertiary_collection(request):
    return store_registration(TertiaryCollectionSerializer, request)

@api_view(['POST'])
def create_customer_collection(request):
    return store_registration(CustomerCollectionSerializer, request)


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
def get_primary_collections(request, id):
    return get_store(request, id, PrimaryCollection, PrimaryCollectionSerializer)

@api_view(['GET'])
def get_secondary_collection(request, id):
    return get_store(request, id, SecondaryCollection, SecondaryCollectionSerializer)

@api_view(['GET'])
def get_tertiary_collections(request, id):
    return get_store(request, id, TertiaryCollection, TertiaryCollectionSerializer)

@api_view(['GET'])
def get_customer_collection(request, id):
    return get_store(request, id, CustomerCollection, CustomerCollectionSerializer)




#.......................................EDIT STORE DATA.......................................

def update_data(request, id, queryset, serializer_class):
    user_profiles_info_update = queryset.objects.get(pk=id)
    serializer = serializer_class(
        instance=user_profiles_info_update, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def edit_primary_collection(request, id):
    return update_data(request, id, PrimaryCollection, PrimaryCollectionSerializer)

@api_view(['PUT'])
def edit_secondary_collection(request, id):
    return update_data(request, id, SecondaryCollection, SecondaryCollectionSerializer)

@api_view(['PUT'])
def edit_tertiary_collection(request, id):
    return update_data(request, id, TertiaryCollection, TertiaryCollectionSerializer)

@api_view(['PUT'])
def edit_customer_collection(request, id):
    return update_data(request, id, CustomerCollection, CustomerCollectionSerializer)




#.......................................DELETE STORE DATA.......................................

def delete_collection(request, id, queryset):
    delete_store_info = queryset.objects.get(pk=id)
    delete_store_info.delete()
    return Response("This store has been successfully deleted")

@api_view(['DELETE'])
def delete_primary_collection(request, id):
    return delete_collection(request, id, PrimaryCollection)

@api_view(['DELETE'])
def delete_secondary_collection(request, id):
    return delete_collection(request, id, SecondaryCollection)

@api_view(['DELETE'])
def delete_tertiary_collection(request, id):
    return delete_collection(request, id, TertiaryCollection)

@api_view(['DELETE'])
def delete_customer_collection(request, id):
    return delete_collection(request, id, CustomerCollection)