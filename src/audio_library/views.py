import os

from django.db.models import F
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics, parsers, views, viewsets
from src.base.classes import MixedSerializer, Pagination
from src.base.services import delete_old_file

from ..base.permissions import IsAuthor
from . import models, serializer


class GenreView(generics.ListAPIView):
    """List of genres
    """
    queryset = models.Genre.objects.all()
    serializer_class = serializer.GenreSerializer


class LicenseView(viewsets.ModelViewSet):
    """List of licenses
    """
    queryset = models.License.objects.all()
    serializer_class = serializer.LicenseSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumView(viewsets.ModelViewSet):
    """CRUD for author albums
    """
    queryset = models.Album.objects.all()
    parser_classes = [parsers.MultiPartParser]
    serializer_class = serializer.AlbumSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        delete_old_file(instance.cover.path)
        instance.delete()


class PublicAlbumView(generics.ListAPIView):
    """List of author public albums
    """
    serializer_class = serializer.AlbumSerializer
    queryset = models.Album.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user__id=self.kwargs.get('pk'), private=False)


class TrackView(MixedSerializer, viewsets.ModelViewSet):
    """CRUD for tracks
    """
    queryset = models.Track.objects.all()
    parser_classes = [parsers.MultiPartParser]
    permission_classes = [IsAuthor]
    serializer_class = serializer.CreateAuthorTrackSerializer
    serializer_classes_by_action = {
        'list': serializer.AuthorTrackSerializer
    }

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        delete_old_file(instance.cover.path)
        instance.delete()


class PlayListView(viewsets.ModelViewSet):
    """CRUD for user playlists
    """
    queryset = models.Playlist.objects.all()
    parser_classes = [parsers.MultiPartParser]
    permission_classes = [IsAuthor]
    serializer_class = serializer.CreatePlayListSerializer
    serializer_classes_by_action = {
        'list': serializer.AuthorTrackSerializer
    }

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TrackListView(generics.ListAPIView):
    """List of all tracks
    """
    queryset = models.Track.objects.all()
    serializer_class = serializer.AuthorTrackSerializer
    pagination_class = Pagination


class AuthorTrackListView(generics.ListAPIView):
    """List of author tracks
    """
    queryset = models.Track.objects.all()
    serializer_class = serializer.AuthorTrackSerializer
    pagination_class = Pagination

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class StreamingFileView(views.APIView):

    def set_play(self, track):
        track.plays_count = F('plays_count') + 1
        track.save()

    def get(self, request, pk):
        track = get_object_or_404(models.Track, id=pk)

        if os.path.exists(track.file.path):
            self.set_play(track)

            return FileResponse(open(track.file.path), 'rb', filename=track.file.name)
        else:
            return Http404


class DownloadTrackView(views.APIView):
    def set_download(self):
        self.track.download = F('download') + 1
        self.track.save()

    def get(self, request, pk):
        self.track = get_object_or_404(models.Track, id=pk)

        if os.path.exists(self.track.file.path):
            self.set_download(self.track)

            return FileResponse(open(self.track.file.path), 'rb', filename=self.track.file.name, as_attachment=True)
        else:
            return Http404
