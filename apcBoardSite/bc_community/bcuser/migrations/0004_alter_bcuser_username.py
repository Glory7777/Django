# Generated by Django 4.2.3 on 2023-07-25 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bcuser', '0003_alter_bcuser_useremail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bcuser',
            name='username',
            field=models.CharField(max_length=32, verbose_name='사용자명'),
        ),
    ]
