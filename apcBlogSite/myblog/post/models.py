from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title=models.CharField(max_length=200, verbose_name='제목')
    body=models.TextField(verbose_name='본문')
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    author=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='포스트'
        verbose_name_plural='포스트들'
        