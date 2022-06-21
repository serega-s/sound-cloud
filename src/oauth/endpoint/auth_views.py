from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from .. import serializer
from ..services.google import check_google_auth


def google_login(request):
    """Google signin page
    """

    return render(request, 'oauth/google_login.html')


@api_view(['POST'])
def google_auth(request):
    """Auth confirmation with Google
    """
    google_data = serializer.GoogleAuth(data=request.data)

    if google_data.is_valid():
        token = check_google_auth(google_data.data)
        return Response(token)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN, data='Bad Google data')
