# Generated by Django 4.2.3 on 2023-07-27 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bcuser', '0004_alter_bcuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bcuser',
            name='username',
            field=models.CharField(max_length=64, verbose_name='사용자명'),
        ),
    ]
