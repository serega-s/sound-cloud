from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    """File path building, format: (media)/avatar/user_id/photo.jpeg
    """
    return f'avatar/{instance.id}/{file}'


def validate_size_image(file_obj):
    """File size checking
    """
    megabyte_limit = 2

    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Max file size {megabyte_limit}MB")
