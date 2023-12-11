from django.urls import path
from . import views

urlpatterns = [
    path('all-primary-products', views.get_all_primary_products),
    path('all-secondary-products', views.get_all_secondary_products),
    path('all-tertiary-products', views.get_all_tertiary_products),
    path('all-products', views.get_all_products),


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
