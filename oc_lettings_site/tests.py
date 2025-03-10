import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_view(client):
    """
    Test the index view.

    Ensures that the index page is accessible and returns a 200 status code.
    """
    response = client.get(reverse("index"))
    assert response.status_code == 200
    assert b"Welcome to Holiday Homes" in response.content


@pytest.mark.django_db
def test_custom_404(client):
    """
    Test the custom 404 view.

    Ensures that a non-existent page returns a custom 404 error.
    """
    response = client.get("/non-existent-page/")
    assert response.status_code == 404
    assert b"404" in response.content
