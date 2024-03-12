from django.urls import path
from . import views

urlpatterns = [
    path('all-primary-collections', views.get_all_primary_collections),
    path('all-secondary-collections', views.get_all_secondary_collections),
    path('all-tertiary-collections', views.get_all_tertiary_collections),
    path('all-customer-collections', views.get_all_customer_collections),

    path('create-primary-collection', views.create_primary_collection),
    path('create-secondary-collection', views.create_secondary_collection),
    path('create-tertiary-collection', views.create_tertiary_collection),
    path('create-customer-collection', views.create_customer_collection),

    path('get-primary-collections/<int:store_id>/',
         views.get_primary_collections),
    path('get-secondary-collections/<int:store_id>/',
         views.get_secondary_collection),
    path('get-tertiary-collections/<int:store_id>/',
         views.get_tertiary_collections),
    path('get-customer-collections/<int:customer_id>/',
         views.get_customer_collection),


    path('edit-primary-collections/<int:id>/', views.edit_primary_collection),
    path('edit-secondary-collections/<int:id>/',
         views.edit_secondary_collection),
    path('edit-tertiary-collections/<int:id>/', views.edit_tertiary_collection),
    path('edit-customer-collections/<int:id>/', views.edit_customer_collection),


    path('delete-primary-collections/<int:id>/',
         views.delete_primary_collection),
    path('delete-secondary-collections/<int:id>/',
         views.delete_secondary_collection),
    path('delete-tertiary-collections/<int:id>/',
         views.delete_tertiary_collection),
    path('delete-customer-collections/<int:id>/',
         views.delete_customer_collection),
]
