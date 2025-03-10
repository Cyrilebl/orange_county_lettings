"""
Main URL configuration for the project.

This module defines the URL routing.
It includes paths for the admin panel, the homepage, and the `lettings` and `profiles` apps.
Additionally, it specifies custom error handlers for 404 and 500 errors.

If the `DEBUG` setting is enabled, static files are served using Django's `static()` helper.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

# Custom error handlers
handler404 = views.custom_404
handler500 = views.custom_500


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
]

# Serve static files in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
