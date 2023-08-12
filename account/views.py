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
from .utils import SessionCsrfExemptAuthentication
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

# Create your views here.
class CustomTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)

class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = (AllowAny,)

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

            token = str(RefreshToken.for_user(user))

            return Response({"token":token}, status=status.HTTP_201_CREATED)

        


