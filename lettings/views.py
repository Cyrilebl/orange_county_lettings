from django.shortcuts import render
from .models import Letting


def index(request):
    """
    Display the list of all lettings.

    Retrieves all Letting objects from the database and passes them to the template.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered lettings index page.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Display the details of a specific letting.

    Retrieves a Letting object based on the provided letting ID and passes
    its details to the template.

    Args:
        request: The HTTP request object.
        letting_id (int): The ID of the letting to retrieve.

    Returns:
        HttpResponse: The rendered letting detail page.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
