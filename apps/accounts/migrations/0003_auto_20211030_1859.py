# Generated by Django 3.2 on 2021-10-30 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birth_day',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='weight',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
