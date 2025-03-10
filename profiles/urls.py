"""
This module defines URL patterns for the Profiles application,
mapping views to specific endpoints.
"""

from django.urls import path

from . import views

app_name = "profiles"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:username>/", views.profile, name="profile"),
]
