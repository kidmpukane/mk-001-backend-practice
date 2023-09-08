from django.urls import path
from . import views

urlpatterns = [
    path('all-user-profiles', views.get_user_data),
    path('register-new-user/', views.register_user),
    path('user-profile/<int:id>/', views.get_user_profile),
    path('update/<int:id>/', views.update_user_data),
    path('delete/<int:id>/', views.delete_user_data),
]
