from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('list/', views.board_list),  # 127.0.0.1:8000/board/list
    path('write/', views.board_write),
    path('detail/<int:pk>/', views.board_detail)
]