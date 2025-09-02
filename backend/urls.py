from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Docs",
        default_version='v1',
    ),
    public=True,
)

urlpatterns = [
    path('', include('api.urls')),
    path('swagger/', schema_view.with_ui('swagger'), name='schema-swagger-ui')
]
