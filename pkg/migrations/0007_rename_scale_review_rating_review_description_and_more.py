# Generated by Django 4.0.6 on 2022-08-17 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkg', '0006_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='scale',
            new_name='rating',
        ),
        migrations.AddField(
            model_name='review',
            name='description',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
