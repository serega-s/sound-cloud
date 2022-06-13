from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import permissions
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path(
        'openapi/',
        get_schema_view(
            title="Audio Library",
            description="Audio Library backend built with DRF",
            version="1.0.0",
            permission_classes=[permissions.AllowAny],
        ),
        name='openapi-schema'
    ),
    path(
        'docs/',
        TemplateView.as_view(
            template_name='swagger/swagger-ui.html',
            extra_context={'schema_url': 'openapi-schema'}
        ),
        name='swagger-ui'
    ),
    path('auth/', include('src.oauth.urls'))
]
