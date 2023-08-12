from django.contrib import admin
from .models import TrayItem, Station, Meal, Order

# Register your models here.
admin.site.register(Station)
admin.site.register(TrayItem)
admin.site.register(Meal)
admin.site.register(Order)