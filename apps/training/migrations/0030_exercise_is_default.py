# Generated by Django 3.2 on 2021-11-21 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0029_exerciseroutine_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
    ]