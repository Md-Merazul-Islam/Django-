# Generated by Django 5.0.4 on 2024-05-09 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
        ('cars', '0008_alter_car_brand_delete_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='brand',
        ),
        migrations.AddField(
            model_name='car',
            name='brand',
            field=models.ManyToManyField(to='brand.brand'),
        ),
    ]