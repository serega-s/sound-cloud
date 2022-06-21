from rest_framework import parsers, permissions, viewsets

from ...base.permissions import IsAuthor
from .. import models, serializer


class UserView(viewsets.ModelViewSet):
    """View and edit user
    """
    parser_classes = [parsers.MultiPartParser]
    serializer_class = serializer.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user

    def get_object(self):
        return self.get_queryset()


class AuthorView(viewsets.ModelViewSet):
    """ List of authors
    """
    queryset = models.AuthUser.objects.all().prefetch_related('social_links')
    serializer_class = serializer.AuthorSerializer


class SocialLinkView(viewsets.ModelViewSet):
    """ CRUD for user social links
    """
    serializer_class = serializer.SocialLinkSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return self.request.user.social_links.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
