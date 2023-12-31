# Generated by Django 4.2.3 on 2023-07-27 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bcuser', '0001_initial'),
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='제목')),
                ('contents', models.TextField(verbose_name='내용')),
                ('register_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('tags', models.ManyToManyField(to='tag.tag', verbose_name='태그')),
                ('write', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bcuser.bcuser', verbose_name='작성자')),
            ],
            options={
                'verbose_name': '부트캠퍼스 게시글',
                'verbose_name_plural': '부트캠퍼스 게시글',
                'db_table': 'bootcampus_board',
            },
        ),
    ]
