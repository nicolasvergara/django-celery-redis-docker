# Generated by Django 4.0.4 on 2022-04-20 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0004_alter_bus_driver_alter_ticket_bus_alter_ticket_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='owner',
        ),
    ]
