from django.shortcuts import render
from .models import Profile


def index(request):
    """
    Display the list of all profiles.

    Retrieves all Profile objects from the database and passes them to the template.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered profiles index page.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Display the details of a specific profile.

    Retrieves a Profile object based on the provided username and passes it
    to the template.

    Args:
        request: The HTTP request object.
        username (str): The username of the profile to display.

    Returns:
        HttpResponse: The rendered profile detail page.
    """
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
