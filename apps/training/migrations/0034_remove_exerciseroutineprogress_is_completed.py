# Generated by Django 3.2 on 2021-11-23 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0033_auto_20211122_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exerciseroutineprogress',
            name='is_completed',
        ),
    ]
