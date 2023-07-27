from django.db import models

# Create your models here.

# models.Model : 상속받음
class Bcuser(models.Model):
    # verbose_name : 사용자명
    username=models.CharField(max_length=32, verbose_name='사용자명')
    useremail=models.EmailField(max_length=128, verbose_name='사용자이메일')
    password=models.CharField(max_length=64, verbose_name='비밀번호')
    # auto_now_add : 현재시간 적용
    models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    # username 생성시 문자열 함수를 이용하여 객체 username으로 반환
    def __str__(self):
        return self.username
    
    # Table Name
    class Meta:
        db_table='bootcampus_bcuser'
        verbose_name="부트캠퍼스 사용자"
        verbose_name_plural='부트캠퍼스 사용자'



