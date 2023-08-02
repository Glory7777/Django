from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('list/', views.board_list, name="board_list"),   #127.0.0.1:8000/board/list
    path('write/', views.board_write),
    path('detail/<int:pk>/', views.board_detail), #<int:pk>/ 고유한 id를 가져와서 번호 매김(이후 조회수 판단근거가됨)
    path('update/<int:pk>/', views.board_update, name="board_update"),
    path('delete/<int:pk>/', views.board_delete),
]
