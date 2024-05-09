# Generated by Django 5.0.4 on 2024-05-09 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0012_alter_comment_email_alter_comment_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='car',
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
