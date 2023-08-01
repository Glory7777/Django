from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자') # User가 참조되는 Foreignkey로 user 가 탈퇴하면 게시글 같이 소멸됨 
    title= models.CharField(max_length=200, verbose_name='제목')
    body=models.TextField(verbose_name='내용')
    image=models.ImageField(upload_to='posts/', null=True, blank=True, verbose_name='이미지')
    # 게시물이 생성된 날짜와 시간을 저장. 기본값은 게시물이 생성되는 시점의 시간
    # (default=timezone.now). 이 필드를 명시적으로 설정하지 않으면,
    # 게시물이 데이터베이스에 생성될 때 자동으로 현재 시간으로 설정
    # python -m pip install Pillow             
    created_date= models.DateTimeField(default=timezone.now, verbose_name='작성일') 
    # 게시물이 공개된 날짜와 시간을 저장. 이 필드는 null 허용, 비어 있을 수도 있음.
    publiShed_date=models.DateTimeField(null=True, blank=True, verbose_name='수정일') 

    # black=True : Django에서 폼을 검증할 때 사용, null 값이여도 forms.py에서 검증하라는 뜻
    # 이 속성이 True로 설정되면, 폼에서 이 필드는 선택적인 것이 되고, 사용자는 이 필드를 비워 둘 수 있음.
    # null=True : True로 설정되면, 데이터 베이스에 이 필드는 null값을 가질 수 있음.
    
    
    # 게시글의 날짜와 시간을 설정하고, 그 정보를 데이터베이스에 즉시 반영
    def publiShed(self):
        self.publiShed_date = timezone.now()
        self.save()
    
    def __str__(self): 
        return self.title
    
    class Meta:
        verbose_name='포스트'
        verbose_name_plural='포스트들'


    