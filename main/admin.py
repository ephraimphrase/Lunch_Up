from django.contrib import admin
from .models import Tray, Station, Meal, Order

# Register your models here.
admin.site.register(Station)
admin.site.register(Tray)
admin.site.register(Meal)
admin.site.register(Order)