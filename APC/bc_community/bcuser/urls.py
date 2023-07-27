from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('register/', views.register),  # 127.0.0.1:8000/bcuser/register
    path('login/', views.login),
    path('logout/', views.logout)
]