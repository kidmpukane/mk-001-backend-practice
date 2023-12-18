from rest_framework.decorators import api_view
from rest_framework import status
from keras.datasets import fashion_mnist
from rest_framework.response import Response
from .models import (
    PrimaryProduct,
    SecondaryProduct, 
    TertiaryProduct
)
from .serializers import (
    AllProductsSerializer,
    PrimaryProductSerializer, 
    SecondaryProductSerializer, 
    TertiaryProductSerializer,
    ProductInputSerializer
)
from itertools import chain
from sklearn.neighbors import NearestNeighbors
import numpy as np
from sklearn.preprocessing import StandardScaler
import schedule
import time

#.......................................GET ALL USER DATA.......................................

@api_view(['GET'])
def get_all_products(request):
    primary_products = PrimaryProduct.objects.all()
    secondary_products = SecondaryProduct.objects.all()
    
    primary_serializer = PrimaryProductSerializer(primary_products, many=True)
    secondary_serializer = SecondaryProductSerializer(secondary_products, many=True)
    
    all_products = {
        "all_products": primary_serializer.data + secondary_serializer.data
    }
    
    return Response(all_products)


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


#.......................................CREATE PRODUCT.......................................

def product_registration(serializer_class, request):
    serializer = serializer_class(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_primary_product(request):
    return product_registration(PrimaryProductSerializer, request)

@api_view(['POST'])
def create_secondary_product(request):
    return product_registration(SecondaryProductSerializer, request)

@api_view(['POST'])
def create_tertiary_product(request):
    return product_registration(TertiaryProductSerializer, request)

#.......................................GET USER BY ID.......................................

def get_product(request, id, profile_model, serializer_class):
    try:
        user_profile_data = profile_model.objects.get(pk=id)
    except profile_model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = serializer_class(user_profile_data)
        return Response(serializer.data)

@api_view(['GET'])
def get_primary_product(request, id):
    return get_product(request, id, PrimaryProduct, PrimaryProductSerializer)

@api_view(['GET'])
def get_secondary_product(request, id):
    return get_product(request, id, SecondaryProduct, SecondaryProductSerializer)

@api_view(['GET'])
def get_tertiary_product(request, id):
    return get_product(request, id, TertiaryProduct, TertiaryProductSerializer)


#.......................................GET PRODUCT BY ID........................................

@api_view(['GET'])
def get_primary_product(request, primary_id):
    try:
        primary_product_data, similar_primary_products = get_product_and_similars(primary_id, PrimaryProduct)

        response_data = {
            "primary_product": primary_product_data,
            "similar_primary_products": similar_primary_products
        }

        return Response(response_data)

    except PrimaryProduct.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_secondary_product(request, secondary_id):
    try:
        secondary_product_data, similar_secondary_products = get_product_and_similars(secondary_id, SecondaryProduct)

        response_data = {
            "secondary_product": secondary_product_data,
            "similar_secondary_products": similar_secondary_products
        }

        return Response(response_data)

    except SecondaryProduct.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
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


#.......................................GET 5 NEAREST NEIGHBOR........................................


def get_all_products_features():
    primary_feature_lists = list(PrimaryProduct.objects.values_list('feature_list', flat=True))
    secondary_feature_lists = list(SecondaryProduct.objects.values_list('feature_list', flat=True))
    all_feature_lists = list(chain(primary_feature_lists, secondary_feature_lists))
    return all_feature_lists

def train_knn_model(features):
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    knn = NearestNeighbors(n_neighbors=5)
    knn.fit(scaled_features)
    
    return knn, scaler

@api_view(['POST'])
def find_the_nearest_neighbor(request):
    serializer = ProductInputSerializer(data=request.data)
    if serializer.is_valid():
        input_product = serializer.validated_data

        all_features = get_all_products_features()
        if not all_features:
            return Response("No features found", status=404)

        knn_model, scaler = train_knn_model(all_features)

        input_features = scaler.transform([input_product['feature_list']])
        distances, indices = knn_model.kneighbors(input_features)
        similar_indices = indices[0]

        similar_products_info = []
        for idx in similar_indices:
            product = get_object_or_404(chain(PrimaryProduct.objects.all(), SecondaryProduct.objects.all()), pk=idx)
            product_data = {
                "id": product.id,
                "product_name": product.product_name,
                "product_image": product.product_image,
                # Include other fields as needed
            }
            similar_products_info.append(product_data)

        serializer = AllProductsSerializer(similar_products_info, many=True)
        return Response(serializer.data)

    return Response(serializer.errors, status=400)

# @api_view(['POST'])
# def find_the_nearest_neighbor(request):
#     serializer = ProductInputSerializer(data=request.data)
#     if serializer.is_valid():
#         return Response(serializer.validated_data)
    
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)