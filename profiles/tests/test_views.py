import pytest
from django.urls import reverse
from .test_data import create_user, create_profile


@pytest.mark.django_db
def test_index_view(client):
    """
    Test the index view.

    Ensures that the index page is accessible and returns a 200 status code.
    """
    response = client.get(reverse("profiles:index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_view(client):
    """
    Test the profile detail view.

    Creates a User and a Profile instance, then verifies that the
    profile detail page is accessible and returns a 200 status code.
    """
    user = create_user()
    profile = create_profile(user)

    response = client.get(reverse("profiles:profile", args=[user.username]))
    assert response.status_code == 200
