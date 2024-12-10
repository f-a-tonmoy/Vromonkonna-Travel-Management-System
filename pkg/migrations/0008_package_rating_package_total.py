# Generated by Django 4.0.6 on 2022-08-19 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkg', '0007_rename_scale_review_rating_review_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='rating',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='total',
            field=models.IntegerField(default=0, null=True),
        ),
    ]