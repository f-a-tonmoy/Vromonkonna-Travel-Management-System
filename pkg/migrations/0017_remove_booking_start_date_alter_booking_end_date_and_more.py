# Generated by Django 4.0.6 on 2022-08-20 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkg', '0016_alter_booking_end_date_alter_booking_start_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='start_date',
        ),
        migrations.AlterField(
            model_name='booking',
            name='end_date',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='package',
            name='end_date',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='package',
            name='start_date',
            field=models.CharField(max_length=32),
        ),
    ]
