# Generated by Django 5.0.4 on 2024-05-17 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_userbankaccount_is_bankrupt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbankaccount',
            name='is_bankrupt',
        ),
    ]