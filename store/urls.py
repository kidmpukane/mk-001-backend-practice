from django.urls import path
from . import views

urlpatterns = [
    path('get-all-stores', views.get_all_stores),
    path('register-new-store/', views.register_store),
    path('get-store/<int:merchant_id>/', views.get_store_by_id),
    path('update-store/<int:id>/', views.update_store_data),
    path('delete-store/<int:id>/', views.delete_store),
]
