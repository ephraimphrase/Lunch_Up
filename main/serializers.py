from rest_framework import serializers
from .models import TrayItem, Station, Meal, Order

class TrayItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrayItem
        depth = 1
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
        depth = 2
