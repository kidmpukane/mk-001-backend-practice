from rest_framework.decorators import api_view
from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from .models import Store
from user_profiles.models import Merchant
from .serializers import StoreSerializer
from store_collections.models import PrimaryCollection, SecondaryCollection, TertiaryCollection

# .......................................GET ALL USER DATA.......................................


def get_data(queryset, serializer_class):
    data = queryset.objects.all()
    serializer = serializer_class(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_stores(request):
    return get_data(Store, StoreSerializer)


# .......................................REGISTER STORE.......................................

def store_registration(serializer_class, request):
    serializer = serializer_class(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register_store(request):
    serializer = StoreSerializer(data=request.data)
    if serializer.is_valid():
        store = serializer.save()

        # Create Primary Collection
        PrimaryCollection.objects.create(store_id=store)

        # Create Secondary Collection
        SecondaryCollection.objects.create(store_id=store)

        # Create Tertiary Collection
        TertiaryCollection.objects.create(store_id=store)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# .......................................GET USER BY ID.......................................

@api_view(['GET'])
def get_store_by_id(request, merchant_id):
    try:

        store_query = Store.objects.filter(merchant_id=merchant_id)
    except Store.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StoreSerializer(store_query, many=True)
        return Response(serializer.data)


# .......................................EDIT STORE DATA.......................................

def update_data(request, id, model_class, serializer_class):
    print(request.data)
    try:
        instance = model_class.objects.get(pk=id)
    except model_class.DoesNotExist:
        return Response({"detail": "Not found"}, status=404)

    serializer = serializer_class(instance=instance, data=request.data)

    with transaction.atomic():
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


@api_view(['PUT'])
def update_store_data(request, id):
    return update_data(request, id, Store, StoreSerializer)

# .......................................DELETE STORE DATA.......................................


@api_view(['DELETE'])
def delete_store(request, id):
    delete_store_info = Store.objects.get(pk=id)
    delete_store_info.delete()
    return Response("This store has been successfully deleted")
