# Generated by Django 4.0.6 on 2022-08-13 05:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('destination', models.CharField(max_length=128)),
                ('thoughts', models.TextField(max_length=1024)),
                ('likes', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, default='default_blog.jpg', null=True, upload_to='blogs/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
