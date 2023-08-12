from rest_framework import serializers
from .models import Tray, Station, Meal

class TraySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tray
        fields = '__all__'

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'
