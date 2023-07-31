# Generated by Django 4.2.3 on 2023-07-31 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='제목')),
                ('body', models.TextField(verbose_name='내용')),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/', verbose_name='이미지')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='작성일')),
                ('publicShed_date', models.DateTimeField(blank=True, null=True, verbose_name='수정일')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'verbose_name': '포스트',
                'verbose_name_plural': '포스트들',
            },
        ),
    ]
