from rest_framework import status
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed
from src.oauth import serializer
from src.oauth.models import AuthUser

from google.auth.transport import requests
from google.oauth2 import id_token

from . import base_auth


def check_google_auth(google_user: serializer.GoogleAuth):
    try:
        id_token.verify_oauth2_token(google_user['token'], requests.Request(), settings.GOOGLE_CLIENT_ID)
    except ValueError:
        raise AuthenticationFailed(
            code=status.HTTP_403_FORBIDDEN, data='Bad Google token')

    user, _ = AuthUser.objects.get_or_create(email=google_user['email'])

    return base_auth.create_access_token(user.id)
