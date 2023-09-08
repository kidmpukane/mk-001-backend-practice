from django.urls import path
from . import views

urlpatterns = [
    path('get-stores/<int:id>/', views.get_store_by_id),
]
