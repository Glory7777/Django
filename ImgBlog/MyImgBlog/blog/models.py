from django.db import models
from django import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자') # User가 참조되는 Foreignkey로 user 가 탈퇴하면 게시글 같이 소멸됨 
    title= models.CharField(max_length=200, verbose_name='제목')
    text=models.TextField(verbose_name='내용')
    image=models.ImageField(verbose_name='이미지')
    created_date= models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    publicShed_date=
    
    def __str__(self): 
        return self().title
    
    class Meta:
        verbose_name='포스트'
        verbose_name_plural='포스트들'


    