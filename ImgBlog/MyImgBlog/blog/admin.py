from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=('title', 'body','image') #admin등록시 노출정보

admin.site.register(Post, PostAdmin) #DB Post를 admin에 등록