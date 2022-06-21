from datetime import datetime, timezone
from typing import Optional

import jwt
from django.conf import settings
from ..models import AuthUser
from rest_framework import authentication, exceptions


class AuthBackend(authentication.BaseAuthentication):
    authentication_header_prefix = 'Token'

    def authenticate(self, request, token=None, **kwargs) -> Optional[tuple]:
        auth_header = authentication.get_authorization_header(request).split()

        if not auth_header or auth_header[0].lower() != b'token':
            return None

        if len(auth_header) == 1:
            raise exceptions.AuthenticationFailed(
                'Invalid token header. No credential provided.')
        elif len(auth_header) > 2:
            raise exceptions.AuthenticationFailed(
                'Invalid token header. Token string should not contain spaces.')

        try:
            token = auth_header[1].decode('utf-8')

        except UnicodeError as e:
            raise exceptions.AuthenticationFailed(
                'Invalid token header. Token string shoul not contain invalid characters.') from e

        return self.authenticate(token)

    def authenticate_credential(self, token) -> tuple:
        try:
            payload = jwt.decode(token, settings.SECRET_KEY,
                                 algorithms=settings.ALGORITHM)
        except jwt.PyJWTError as e:
            raise exceptions.AuthenticationFailed(
                'Invalid authentication. Could not decode token.') from e

        token_exp = datetime.fromtimestamp(payload['exp'])
        if token_exp < datetime.now(timezone.utc):
            raise exceptions.AuthenticationFailed(
                'Token expired.')

        try:
            user = AuthUser.objects.get(id=payload['user_id'])
        except AuthUser.DoesNotExist as exc:
            raise exceptions.AuthenticationFailed('No user matching this token was found.') from exc

        return user, None