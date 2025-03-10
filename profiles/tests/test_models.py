import pytest
from .test_data import create_user, create_profile


@pytest.mark.django_db
def test_create_profile():
    """
    Test the creation of a Profile instance.
    """
    user = create_user()
    profile = create_profile(user)

    assert profile.user == user
    assert profile.favorite_city == "Madrid"
