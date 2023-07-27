from django.db import models

# Create your models here.
# models.Model : 상속받음
class Board(models.Model):
    title=models.CharField(max_length=128, verbose_name='제목')
    contents=models.TextField(verbose_name='내용')
    write=models.ForeignKey('bcuser.Bcuser', on_delete=models.CASCADE, verbose_name='작성자')
    # auto_now_add : 현재시간 적용
    register_dttm=models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.title
    
    # Table Name
    class Meta:
        db_table='bootcampus_board'
        verbose_name="부트캠퍼스 게시글"
        verbose_name_plural='부트캠퍼스 게시글'

