from django.urls import path
from . import views


urlpatterns = [
    path('api/register/', views.RegisterView.as_view()),
    path('api/login/', views.CustomTokenPairView.as_view()),
    path('api/refresh/', views.CustomTokenRefreshView.as_view())
]