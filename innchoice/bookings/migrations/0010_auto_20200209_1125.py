# Generated by Django 3.0.2 on 2020-02-09 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0009_auto_20200209_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='checkin',
        ),
        migrations.RemoveField(
            model_name='room',
            name='checkout',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_type',
        ),
    ]