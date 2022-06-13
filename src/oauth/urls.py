from django.urls import path

from .endpoint import auth_views, views

urlpatterns = [
    path('', auth_views.google_login, name='google_login'),
    path('google/', auth_views.google_auth, name='google_auth')
]
