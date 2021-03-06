# Generated by Django 4.0.5 on 2022-06-22 12:49

import django.core.validators
from django.db import migrations, models
import src.base.services


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=src.base.services.get_path_upload_avatar, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg']), src.base.services.validate_size_image]),
        ),
    ]
