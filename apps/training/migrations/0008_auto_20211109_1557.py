# Generated by Django 3.2 on 2021-11-09 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0007_remove_routine_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcerciseRoutine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('day', models.CharField(blank=True, choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], max_length=30, null=True)),
                ('cycles', models.IntegerField(blank=True, null=True)),
                ('repetitions', models.IntegerField(blank=True, null=True)),
                ('minutes', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.exercise')),
                ('routine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.routine')),
            ],
        ),
        migrations.DeleteModel(
            name='EventExcercise',
        ),
    ]