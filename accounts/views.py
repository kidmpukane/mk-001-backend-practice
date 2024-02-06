from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib import auth
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from user_profiles.models import Merchant, Customer
from .serializers import UserSerializer
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.sessions.models import Session


@method_decorator(csrf_protect, name='dispatch')
class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        username = data['username']
        password = data['password']
        re_password = data['re_password']

        try:
            if password == re_password:
                if User.objects.filter(username=username).exists():
                    return Response({'error': 'Username already exists'})
                else:
                    if len(password) < 6:
                        return Response({'error': 'Password must be at least 6 characters'})
                    else:
                        # Create a new user
                        user = User.objects.create_user(
                            username=username, password=password)

                        # Log in the user
                        auth_user = authenticate(
                            request, username=username, password=password)
                        if auth_user is not None:
                            login(request, auth_user)

                            # Store additional information in the session, if needed
                            request.session['user_id'] = user.id
                            request.session['username'] = user.username

                            return Response({'success': 'User created and logged in successfully'})
                        else:
                            return Response({'error': 'Error authenticating user'})
            else:
                return Response({'error': 'Passwords do not match'})
        except:
            return Response({'error': 'Something went wrong when registering account'})


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        return Response({'success': 'CSRF cookie set'})


class LoginView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        username = data['username']
        password = data['password']

        try:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                # Generate CSRF token and add it to the session
                csrf_token = get_token(request)
                request.session['csrf_token'] = csrf_token

                # Store user information in the session
                request.session['user_id'] = user.id
                request.session['username'] = user.username

                # Return the CSRF token and session ID in the response
                return Response({
                    'success': 'User has been authenticated',
                    'user_id': user.id,
                    'csrf_token': csrf_token,
                    'sessionid': request.session.session_key
                })
            else:
                return Response({'error': 'Error authenticating user'})
        except:
            return Response({'error': 'Something went wrong when logging in'})
