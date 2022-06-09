from django.urls import path

from .endpoint import auth_views, views

urlpatterns = [
    path('', auth_views.google_login)
]