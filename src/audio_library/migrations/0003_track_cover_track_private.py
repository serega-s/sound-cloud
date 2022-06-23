# Generated by Django 4.0.5 on 2022-06-22 12:49

import django.core.validators
from django.db import migrations, models
import src.base.services


class Migration(migrations.Migration):

    dependencies = [
        ('audio_library', '0002_rename_title_album_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=src.base.services.get_path_upload_cover_track, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg']), src.base.services.validate_size_image]),
        ),
        migrations.AddField(
            model_name='track',
            name='private',
            field=models.BooleanField(default=False),
        ),
    ]
