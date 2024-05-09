# Generated by Django 5.0.4 on 2024-05-09 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
