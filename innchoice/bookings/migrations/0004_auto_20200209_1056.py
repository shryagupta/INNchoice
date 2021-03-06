# Generated by Django 3.0.2 on 2020-02-09 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='checkout',
        ),
        migrations.AddField(
            model_name='room',
            name='availableno',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='booked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='end_time',
            field=models.TimeField(default=11),
        ),
        migrations.AddField(
            model_name='room',
            name='start_time',
            field=models.TimeField(default=10),
        ),
    ]
