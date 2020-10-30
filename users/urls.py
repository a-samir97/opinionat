from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
]