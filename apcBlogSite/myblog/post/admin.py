from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post) #데이터 베이스 Post를  admin 사이트에 등록
admin.site.register(Comment) #데이터 베이스 Comment를  admin 사이트에 등록

