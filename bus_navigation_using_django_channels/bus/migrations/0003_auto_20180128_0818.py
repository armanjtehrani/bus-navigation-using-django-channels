# Generated by Django 2.0.1 on 2018-01-28 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0002_auto_20180125_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='speed',
            field=models.FloatField(default=0.000535),
        ),
    ]
