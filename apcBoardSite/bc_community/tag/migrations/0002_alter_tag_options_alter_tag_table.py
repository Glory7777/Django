# Generated by Django 4.2.3 on 2023-07-27 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '부트캠퍼스 태그', 'verbose_name_plural': '부트캠퍼스 태그'},
        ),
        migrations.AlterModelTable(
            name='tag',
            table='bootcampus_tag',
        ),
    ]
