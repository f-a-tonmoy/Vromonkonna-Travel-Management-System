# Generated by Django 4.0.6 on 2022-08-19 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pkg', '0009_rename_consumer_review_traveler'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='title',
        ),
    ]
