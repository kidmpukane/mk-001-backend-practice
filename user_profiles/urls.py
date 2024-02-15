from django.urls import path
from .views import (
    get_all_merchant_data,
    get_all_customer_data,
    register_merchant,
    register_customer,
    get_customer_profile,
    get_merchant_profile,
    update_merchant_data,
    update_customer_data,
    delete_user_data,
    UpdateMerchantData,
    UpdateCustomerData,
)

urlpatterns = [
    path('all-merchant-profiles', get_all_merchant_data),
    path('all-customer-profiles', get_all_customer_data),
    path('register-new-merchant/', register_merchant),
    path('register-new-customer/', register_customer),
    path('customer-profile/<int:id>/', get_customer_profile),
    path('merchant-profile/<int:id>/', get_merchant_profile),
    path('update-merchant-profile/<int:id>/', update_merchant_data),
    path('update-customer-profile/<int:id>/', update_customer_data),
    path('delete/<int:id>/', delete_user_data),

    path('merchant-profile-update/<int:id>/',
         UpdateMerchantData.as_view(), name='update-merchant-profile'),
    path('customer-profile-update/<int:id>/',
         UpdateCustomerData.as_view(), name='update-customer-profile'),
]
