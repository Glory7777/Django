from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자') # User가 참조되는 Foreignkey로 user 가 탈퇴하면 게시글 같이 소멸됨 
    title= models.CharField(max_length=200, verbose_name='제목')
    body=models.TextField(verbose_name='내용')
    image=models.ImageField(upload_to='posts/', null=True, blank=True, verbose_name='이미지')
    # python -m pip install Pillow             
    created_date= models.DateTimeField(default=timezone.now, verbose_name='작성일') # 게시물이 데이터베이스에 생성될 때 자동으로 현재 시간으로 설정
    publicShed_date=models.DateTimeField(null=True, blank=True, verbose_name='수정일') # 게시물이 공개된 날짜와 시간을 저장. 이 필드는 null 허용
    # null=True : null값 허용
    # black=True : 폼을 검증하라는 뜻
    
    def publicShed(self):
        self.publicShed_date = timezone.now()
        self.save()
    
    def __str__(self): 
        return self().title
    
    class Meta:
        verbose_name='포스트'
        verbose_name_plural='포스트들'


    