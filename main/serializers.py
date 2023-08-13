from rest_framework import serializers
from .models import TrayItem, Station, Meal, Order

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

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
