from django.urls import path
from . import views

urlpatterns = [
    path('all-primary-products', views.get_all_primary_products),
    path('all-secondary-products', views.get_all_secondary_products),
    path('all-tertiary-products', views.get_all_tertiary_products),
    path('all-products', views.get_all_products),

    path('find-nearest-neighbors', views.find_the_nearest_neighbor),

    path('primary_product/<int:primary_id>/', views.get_primary_product),
    path('secondary_product/<int:secondary_id>/', views.get_secondary_product),

    path('primary-products-for-collections/<int:collection_id>/',
         views.get_primary_product_for_collection),
    path('secondary-products-for-collections/<int:collection_id>/',
         views.get_secondary_product_for_collection),


    path('create-primary-product', views.create_primary_product),
    path('create-secondary-product', views.create_secondary_product),
    path('create-tertiary-product', views.create_tertiary_product),


    path('get-primary-product/<int:id>/', views.get_primary_product),
    path('get-secondary-product/<int:id>/', views.get_secondary_product),
    path('get-tertiary-product/<int:id>/', views.get_tertiary_product),


    path('edit-primary-product/<int:id>/', views.edit_primary_product),
    path('edit-secondary-product/<int:id>/', views.edit_secondary_product),
    path('edit-tertiary-product/<int:id>/', views.edit_tertiary_product),


    path('delete-primary-product/<int:id>/', views.delete_primary_product),
    path('delete-secondary-product/<int:id>/', views.delete_secondary_product),
    path('delete-tertiary-product/<int:id>/', views.delete_tertiary_product),

]
