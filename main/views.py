from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
import jwt
from datetime import datetime, timedelta
from .models import Meal, Tray, Station
from .serializers import TraySerializer, StationSerializer, MealSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class TrayView(APIView):
    def post(self, request, meal_id):
        meal = get_object_or_404(Meal, id=meal_id)
        tray, created = Tray.objects.get_or_create(owner=request.user, meal=meal)

        if not created:
            tray.quantity += 1
            tray.save()
        
        return Response({'message':'Added to Cart'}, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        tray = Tray.objects.get(owner=request.user)
        serializer = TraySerializer(tray, many=True)

        return Response(serializer.data)
    
    def delete(self, request, pk):
        tray = Tray.objects.get(id=pk)
        tray.delete()
        return Response(status=status.HTTP_200_OK)
    
class StationView(APIView):
    def get(self, request):
        station = Station.objects.all()
        serializer = StationSerializer(station, many=True)

        return Response(serializer.data)

class MealView(APIView):
    def get(self, request, station):
        meal = Meal.objects.get(station=station)
        serializer = MealSerializer(meal, many=True)

        return Response(serializer.data)    