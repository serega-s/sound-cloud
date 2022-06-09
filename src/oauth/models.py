from django.core.validators import FileExtensionValidator
from django.db import models

from src.base.service import get_path_upload_avatar, validate_size_image


class AuthUser(models.Model):
    """User model for platform
    """
    email = models.EmailField(max_length=150, unique=True)
    join_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    bio = models.CharField(max_length=2000, blank=True, null=True)
    display_name = models.CharField(max_length=30, blank=True, null=True)
    avatar = models.ImageField(
        upload_to=get_path_upload_avatar,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg']), validate_size_image]
    )

    """Always return True, lets us know if user is authenticated
    """
    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return f'{self.email}'


class Follower(models.Model):
    """Django ORM Model of followers
    """
    user = models.ForeignKey(
        AuthUser, on_delete=models.CASCADE, related_name='owner')
    subscriber = models.ForeignKey(
        AuthUser, on_delete=models.CASCADE, related_name='subscribers')

    def __str__(self):
        return f'{self.subscriber} subscribed {self.user}'


# class SocialLink(models.Model):
#     """Model of user social networks
#     """

#     user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='social_links')
#     link = models.URLField(max_length=100)

#     def __str__(self):
#         return f'{self.user}'
