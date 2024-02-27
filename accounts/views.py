from .models import CustomUser
from django.contrib import auth
from django.http import JsonResponse
from rest_framework.views import APIView
from django.middleware.csrf import get_token
from rest_framework.response import Response
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from rest_framework.decorators import api_view
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from user_profiles.models import Merchant, Customer
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from user_profiles.serializers import MerchantSerializer, CustomerSerializer


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        csrf_token = get_token(request)
        response_data = {'success': 'CSRF cookie set',
                         'csrf_token': csrf_token}
        return JsonResponse(response_data)


@method_decorator(csrf_protect, name='dispatch')
class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        email = data['email']
        password = data['password']
        re_password = data['re_password']

        try:
            if password == re_password:
                if CustomUser.objects.filter(email=email).exists():
                    return Response({'error': 'Email already exists'})
                else:
                    if len(password) < 6:
                        return Response({'error': 'Password must be at least 6 characters'})
                    else:
                        user = CustomUser.objects.create_user(
                            email=email, password=password)

                        # Authenticate and login the user
                        auth_user = authenticate(
                            request, email=email, password=password)
                        if auth_user is not None:
                            login(request, auth_user)

                        # Add any additional profile creation logic here if needed

                        return Response({'success': 'User created and logged in successfully'})
            else:
                return Response({'error': 'Passwords do not match'})
        except Exception as e:
            return Response({'error': f'Something went wrong when registering account: {str(e)}'})


class LoginView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        email = data['email']
        password = data['password']

        try:
            user = auth.authenticate(email=email, password=password)

            if user is not None:
                auth.login(request, user)
                return Response({'success': 'User authenticated'})
            else:
                return Response({'error': 'Error Authenticating'})
        except:
            return Response({'error': 'Something went wrong when logging in'})

# --------------------------------------------GET USER----------------------------------------------


@api_view(['GET'])
def get_customer_by_id(request, user):
    try:
        store_query = Customer.objects.get(user=user)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(store_query)
        return Response(serializer.data)


@api_view(['GET'])
def get_merchant_by_id(request, user):
    try:

        store_query = Merchant.objects.filter(user=user)
    except Merchant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MerchantSerializer(store_query, many=True)
        return Response(serializer.data)
