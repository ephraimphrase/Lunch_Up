from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from rest_framework.response import Response
from rest_framework import generics, status
import jwt
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from .utils import SessionCsrfExemptAuthentication

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        try:
            user = User.objects.get(username=username)

            return Response({"error":"User Already Exists"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()

            expiration_time = datetime.utcnow() + timedelta(hours=1)

            # Create the payload containing the user data and expiration time
            payload = {
                'user_id': user.id,
                'username': user.username,
                'exp': expiration_time,
            }

            # Generate the JWT token using the SECRET_KEY from Django settings
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

            login(request, user)

            return Response({"token":token}, status=status.HTTP_201_CREATED)

@authentication_classes([SessionCsrfExemptAuthentication])
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=username)

            user = authenticate(request, username=username, password=password)

            if user is not None:
                expiration_time = datetime.utcnow() + timedelta(hours=1)

                # Create the payload containing the user data and expiration time
                payload = {
                    'user_id': user.id,
                    'username': user.username,
                    'exp': expiration_time,
                }

                # Generate the JWT token using the SECRET_KEY from Django settings
                token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

                login(request, user)
                return Response({"message":"Logged In successfully", "token":token}, status=status.HTTP_200_OK)
        except:
            return Response({"error":"User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        


