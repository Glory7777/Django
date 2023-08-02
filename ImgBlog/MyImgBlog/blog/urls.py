from django.urls import path
from .import views

urlpatterns = [
    path('<int:pk>/edit/', views.post_edit, name="post_edit"),
    path('', views.post_list, name="post_list"),
    path('new/', views.post_new, name="post_new"),
    path('<int:pk>/', views.post_detail, name="post_detail"),
    path('<int:pk>/', views.post_delete, name="post_delete"),
]

