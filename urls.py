from django.urls import path
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger documentation configuration
schema_view = get_schema_view(
    openapi.Info(
        title="API Sentinel",
        default_version='v1',
        description="API documentation for the sentinel project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@api-sentinel.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)  

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
    path('api/example/', ExampleAPIView.as_view(), name='example'),  # Example API endpoint
]

class ExampleAPIView(APIView):
    def get(self, request):
        return Response({'message': 'This is an example API endpoint'});
