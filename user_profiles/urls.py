from django.urls import path
from . import views

urlpatterns = [
    path('all-merchant-profiles', views.get_all_merchant_data),
    path('all-customer-profiles', views.get_all_customer_data),
    path('register-new-merchant/', views.register_merchant),
    path('register-new-customer/', views.register_customer),
    path('customer-profile/<int:id>/', views.get_customer_profile),
    path('merchant-profile/<int:id>/', views.get_merchant_profile),
    # path('update-merchant-profile/<int:id>/', views.update_merchant_data),
    # path('update-customer-profile/<int:id>/', views.update_customer_data),
    path('delete/<int:id>/', views.delete_user_data),
]
