from django.urls import path
from . import views

urlpatterns = [
    path('get-primary-collection/<int:store_id>/', views.get_primary_collection),
    path('get-secondary-collection/<int:store_id>/',
         views.get_secondary_collection),
    path('get-tertiary-collection/<int:store_id>/',
         views.get_tertiary_collection),
]
