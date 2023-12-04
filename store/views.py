from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Store
from .serializers import StoreSerializer

#.......................................GET ALL USER DATA.......................................

def get_data(queryset, serializer_class):
    data = queryset.objects.all()
    serializer = serializer_class(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_stores(request):
    return get_data(Store, StoreSerializer)



#.......................................REGISTER STORE.......................................

def store_registration(serializer_class, request):
    serializer = serializer_class(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register_store(request):
    return store_registration(StoreSerializer, request)


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
def get_store_by_id(request, id):
    return get_store(request, id, Store, StoreSerializer)




#.......................................EDIT STORE DATA.......................................

def update_data(request, id, queryset, serializer_class):
    user_profiles_info_update = queryset.objects.get(pk=id)
    serializer = serializer_class(
        instance=user_profiles_info_update, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def update_store_data(request, id):
    return update_data(request, id, Store, StoreSerializer)


#.......................................DELETE STORE DATA.......................................

@api_view(['DELETE'])
def delete_store(request, id):
    delete_store_info = Store.objects.get(pk=id)
    delete_store_info.delete()
    return Response("This store has been successfully deleted")
