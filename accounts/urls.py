from django.urls import path
from .views import SignupView, GetCSRFToken, LoginView, get_customer_by_id, get_merchant_by_id
# , LogoutView, CheckAuthenticatedView, DeleteAccountView


urlpatterns = [
    # path('authenticated', CheckAuthenticatedView.as_view()),
    path('register', SignupView.as_view()),
    path('login', LoginView.as_view()),
    path('get-customer/<int:user>/', get_customer_by_id),
    path('get-merchant/<int:user>/', get_merchant_by_id),
    # path('logout', LogoutView.as_view()),
    # path('delete', DeleteAccountView.as_view()),
    path('csrf_cookie', GetCSRFToken.as_view())
]
