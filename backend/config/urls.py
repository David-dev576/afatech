from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token  # <-- IMPORTANT

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("core.urls")),
    # La route pour se connecter et obtenir le Token
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)