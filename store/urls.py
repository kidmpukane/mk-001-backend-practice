from django.urls import path
from . import views

urlpatterns = [
    path('get-stores/<int:merchant_id>/', views.get_store_by_id),
]
