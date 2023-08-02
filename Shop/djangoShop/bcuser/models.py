from django.db import models

class Bcuser(models.Model):
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=128, verbose_name='비밀번호')
    # 사용자의 등급을 저장하는데 사용 -> 선택 가능한 값은 'admin과 'user'
    level = models.CharField(max_length=8, verbose_name='등급',
                            choices=(
                                ('admin', 'admin'),
                                ('user', 'user')
                            ))
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')