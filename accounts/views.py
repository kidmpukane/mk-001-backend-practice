from .models import CustomUser
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
class SignupView(CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        # Log in the user after successfully creating an account
        if response.status_code == status.HTTP_201_CREATED:
            email = request.data.get('email')
            password = request.data.get('password')

            auth_user = authenticate(request, email=email, password=password)

            if auth_user is not None:
                login(request, auth_user)

                # You can store additional information in the session if needed
                request.session['user_id'] = auth_user.id
                request.session['email'] = auth_user.email

        return response


class LoginView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        email = data.get('email')
        password = data.get('password')

        try:
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)

                # Generate CSRF token and add it to the session
                csrf_token = get_token(request)
                request.session['csrf_token'] = csrf_token

                # Store user information in the session
                request.session['user_id'] = user.id
                # Replace with the correct field if needed
                request.session['email'] = user.email

                # Return the CSRF token and session ID in the response
                return Response({
                    'success': 'User has been authenticated',
                    'user_id': user.id,
                    'csrf_token': csrf_token,
                    'sessionid': request.session.session_key
                })
            else:
                return Response({'error': 'Invalid email or password'})
        except Exception as e:
            return Response({'error': f'Something went wrong when logging in: {str(e)}'})


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
