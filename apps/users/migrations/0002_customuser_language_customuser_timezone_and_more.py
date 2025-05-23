# Generated by Django 5.1.5 on 2025-04-22 15:01

import apps.users.helpers
import apps.users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='language',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='timezone',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.FileField(blank=True, upload_to=apps.users.models._get_avatar_filename, validators=[apps.users.helpers.validate_profile_picture]),
        ),
    ]
