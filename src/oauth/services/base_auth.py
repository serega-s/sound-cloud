from datetime import datetime, timedelta, timezone

import jwt
from django.conf import settings


def create_token(user_id: int) -> dict:
    """ Creating a token
    """
    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTE)

    return {
        'user_id': user_id,
        'access_token': create_access_token(
            data={'user_id': user_id}, expires_delta=access_token_expires
        ),
        'token_type': 'Token'
    }


def create_access_token(data: dict, expires_delta: timedelta = None):
    """Creating access token
    """
    to_encode = data.copy()
    if expires_delta is not None:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode |= {'exp': expire, 'sub': 'access'} # to_encode.update

    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
