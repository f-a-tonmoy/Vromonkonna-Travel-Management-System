# Generated by Django 4.0.6 on 2022-07-22 16:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0002_remove_traveler_dob_traveler_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelrep',
            name='two_factor_auth',
        ),
        migrations.RemoveField(
            model_name='traveler',
            name='two_factor_auth',
        ),
    ]
