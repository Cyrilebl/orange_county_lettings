import pytest
from django.urls import reverse
from .test_data import create_address, create_letting


@pytest.mark.django_db
def test_index_view(client):
    """
    Test the index view.

    Ensures that the index page is accessible and returns a 200 status code.
    """
    response = client.get(reverse("lettings:index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_letting_view(client):
    """
    Test the letting detail view.

    Creates an Address and a Letting instance, then verifies that the
    letting detail page is accessible and returns a 200 status code.
    """
    address = create_address()
    letting = create_letting(address)

    response = client.get(reverse("lettings:letting", args=[letting.id]))
    assert response.status_code == 200
