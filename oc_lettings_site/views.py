"""
This module defines the main views, including:
- The homepage.
- Custom error handlers for 404 and 500 errors.
"""

import sentry_sdk
from django.shortcuts import render


def index(request):
    """
    Render the homepage.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: The rendered index.html template.
    """
    return render(request, "index.html")


def custom_404(request, exception):
    """
    Custom 404 error handler.

    Args:
        request (HttpRequest): The incoming HTTP request.
        exception (Exception): The exception that triggered the 404 error.

    Returns:
        HttpResponse: The rendered 404.html template with a 404 status code.
    """
    return render(request, "404.html", status=404)


def custom_500(request):
    """
    Custom 500 error handler.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: The rendered 500.html template with a 500 status code.
    """
    sentry_sdk.capture_exception()
    return render(request, "500.html", status=500)
