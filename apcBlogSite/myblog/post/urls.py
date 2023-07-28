from django.urls import path
from .import views

urlpatterns = [
    path('', views.post_list, name='post_list'), #127.0.0.1:8000/post/
    path('detail/<int:pk>', views.post_detail, name='post_detail'), #127.0.0.1:8000/post/detail/1
    path('new/', views.post_new, name='post_new'), #127.0.0.1:8000/post/new
]

