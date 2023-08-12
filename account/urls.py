from django.urls import path
from . import views


urlpatterns = [
    path('accounts/register/', views.RegisterView.as_view()),
    path('accounts/login/', views.CustomTokenPairView.as_view()),
    path('accounts/refresh/', views.CustomTokenRefreshView.as_view()),
    path('accounts/logout/', views.LogOutView.as_view()),
    path('accounts/users/<str:pk>/', views.UserDetailView.as_view())
]