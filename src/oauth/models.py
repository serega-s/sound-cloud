from django.core.validators import FileExtensionValidator
from django.db import models


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
        upload_to='',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg'])]
    )

    """Always return True, lets us know if user is authenticated
    """
    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return f'{self.email}'
