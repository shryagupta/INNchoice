# Generated by Django 3.0.2 on 2020-02-22 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='available',
            name='time',
        ),
        migrations.AddField(
            model_name='available',
            name='time',
            field=models.ManyToManyField(to='bookings.timeslots'),
        ),
    ]