from re import T

from django.core.validators import FileExtensionValidator
from django.db import models
from src.oauth.models import AuthUser

from ..base.services import (get_path_upload_avatar,
                             get_path_upload_cover_album,
                             get_path_upload_cover_playlist,
                             get_path_upload_track, validate_size_image)


class License(models.Model):
    # Django ORM Model of track licenses
    user = models.ForeignKey(
        AuthUser, on_delete=models.CASCADE, related_name='licenses')
    text = models.TextField(max_length=1000)

    def __str__(self) -> str:
        return self.text


class Genre(models.Model):
    # Django ORM Model of track genres
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class Album(models.Model):
    # Django ORM Model of track albums
    user = models.ForeignKey(
        AuthUser, on_delete=models.CASCADE, related_name='albums')
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    private = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to=get_path_upload_cover_album,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['jpg', 'jpeg']), validate_size_image
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Track(models.Model):
    """Django ORM Model of track
    """
    user = models.ForeignKey(
        AuthUser, on_delete=models.CASCADE, related_name='tracks')
    title = models.CharField(max_length=50)
    license = models.ForeignKey(
        License, on_delete=models.PROTECT, related_name='license_tracks')
    genre = models.ManyToManyField(Genre, related_name='genre_tracks')
    album = models.ForeignKey(
        Album, on_delete=models.SET_NULL, blank=True, null=True
    )
    link_of_author = models.CharField(max_length=500, blank=True, null=True)
    file = models.FileField(
        upload_to=get_path_upload_track,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['mp3', 'wav'])
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    plays_count = models.PositiveIntegerField(default=0)
    download = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)
    user_of_likes = models.ManyToManyField(
        AuthUser, related_name='likes_of_Tracks')

    def __str__(self) -> str:
        return f'{self.user} - {self.title}'


class Comment(models.Model):
    """Django ORM Model of comment
    """
    user = models.ForeignKey(
        AuthUser, on_delete=models.CASCADE, related_name='comments')
    track = models.ForeignKey(
        Track, on_delete=models.CASCADE, related_name='track_comments')
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)


class Playlist(models.Model):
    """Django ORM Model of playlist
    """
    user = models.ForeignKey(
        AuthUser, on_delete=models.CASCADE, related_name='play_lists')
    title = models.CharField(max_length=50)
    tracks = models.ManyToManyField(Track, related_name='track_play_lists')
    cover = models.ImageField(
        upload_to=get_path_upload_cover_playlist,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['jpg', 'jpeg']), validate_size_image
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
