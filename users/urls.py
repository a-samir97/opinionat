from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupAPIView.as_view(), name='create-user'),
    path('login/', views.LoginAPIView.as_view(),name='login-user')
]
