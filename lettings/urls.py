"""
This module defines URL patterns for the Lettings application,
mapping views to specific endpoints.
"""

from django.urls import path

from . import views

app_name = "lettings"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:letting_id>/", views.letting, name="letting"),
]
