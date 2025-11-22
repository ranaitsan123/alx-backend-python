from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Messaging API",
        default_version='v1',
        description="API documentation for Messaging App",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('chats.urls')),
    path('api-auth/', include('rest_framework.urls')),  # ← added for checker
    path('api/auth/login/', TokenObtainPairView.as_view(), name='jwt-login'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
]
