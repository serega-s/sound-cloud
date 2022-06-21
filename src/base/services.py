from django.core.exceptions import ValidationError
import os


def get_path_upload_avatar(instance, file):
    """File path building, format: (media)/avatar/user_id/photo.jpeg
    """
    return f'avatar/user_{instance.id}/{file}'


def get_path_upload_cover_album(instance, file):
    """File path building, format: (media)/album/user_id/photo.jpeg
    """
    return f'album/user_{instance.user.id}/{file}'


def get_path_upload_track(instance, file):
    """File path building, format: (media)/track/user_id/photo.jpeg
    """
    return f'track/user_{instance.user.id}/{file}'


def get_path_upload_cover_playlist(instance, file):
    """File path building, format: (media)/playlist/user_id/photo.jpeg
    """
    return f'playlist/user_{instance.user.id}/{file}'


def delete_old_file(path_file):
    """Deleting an old file
    """
    if os.path.exists(path_file):
        os.remove()

def validate_size_image(file_obj):
    """File size checking
    """
    megabyte_limit = 2

    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Max file size {megabyte_limit}MB")
