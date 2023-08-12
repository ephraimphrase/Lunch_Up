from django.urls import path
from . import views

urlpatterns = [
    path('api/trayItem/', views.TrayItemView.as_view()),
    path('api/stations/', views.StationView.as_view()),
    path('api/stations/<str:pk>/', views.MealView.as_view()),
]