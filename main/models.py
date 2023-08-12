from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Station(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    cover_art = models.FileField(upload_to='uploads/', blank=True, null=True)
    delivery = models.CharField(max_length=50)
    opening = models.TimeField()
    closing = models.TimeField()

    def __str__(self):
        return self.name
    
class Meal(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    amount = models.CharField(max_length=10, blank=True, null=True)
    cover_art = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.name

class TrayItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.meal.name

class Order(models.Model):
    number = models.CharField(max_length=150)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ManyToManyField(Meal)

    def __str__(self):
        return f'Order {self.number}'