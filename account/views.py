from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from rest_framework.response import Response
from rest_framework import generics, status
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from datetime import datetime, timedelta
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer

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

            refresh = RefreshToken.for_user(user)
            token = str(refresh.access_token)

            return Response({"token":token, "refresh":str(refresh)}, status=status.HTTP_201_CREATED)
        
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])        
class LogOutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message":"Logged out successfully"})

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])  
class UserDetailView(APIView):
    def post(self, request, pk):
        user = User.objects.get(username=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk):
        user = User.objects.get(username=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        user = User.objects.get(username=pk)
        logout(request)
        user.delete()
        return Response({"message":"Account Successfully Deleted"}, status=status.HTTP_200_OK)
        


