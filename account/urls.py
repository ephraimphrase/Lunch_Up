from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/register/', views.RegisterView.as_view()),
    path('api/login/', views.LoginView.as_view())
]