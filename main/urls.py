from django.urls import path
from . import views

urlpatterns = [
    path('api/trayItem/<str:pk>/', views.TrayItemView.as_view()),
    path('api/trayItem/<str:pk>/subtract/', views.SubtractView.as_view()),
    path('api/stations/<str:location>/', views.StationView.as_view()),
    path('api/<str:id>/meals/', views.MealView.as_view()),
    path('api/orders/<str:pk>/', views.OrderView.as_view()),
]