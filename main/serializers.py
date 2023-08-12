from rest_framework import serializers
from .models import TrayItem, Station, Meal

class TrayItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrayItem
        fields = '__all__'

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'
