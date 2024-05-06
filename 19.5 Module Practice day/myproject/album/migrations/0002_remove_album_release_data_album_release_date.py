# Generated by Django 5.0.4 on 2024-05-05 12:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='release_data',
        ),
        migrations.AddField(
            model_name='album',
            name='release_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
