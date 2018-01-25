# Generated by Django 2.0.1 on 2018-01-25 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='my_next_station',
        ),
        migrations.RemoveField(
            model_name='station',
            name='my_prev_station',
        ),
        migrations.AddField(
            model_name='station',
            name='next_station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_prev_station', to='bus.Station'),
        ),
        migrations.AddField(
            model_name='station',
            name='prev_station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_next_station', to='bus.Station'),
        ),
    ]
