# Generated by Django 3.0.2 on 2020-02-22 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20200223_0050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='available',
            name='time',
        ),
        migrations.AddField(
            model_name='available',
            name='time',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='bookings.timeslots'),
            preserve_default=False,
        ),
    ]
