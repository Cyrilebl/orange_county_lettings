from django.contrib.auth.models import User
from profiles.models import Profile


def create_user():
    """
    Create and return a User instance.
    """
    return User.objects.create_user(username="testuser", password="password123")


def create_profile(user):
    """
    Create and return a Profile instance linked to a given User.
    """
    return Profile.objects.create(
        user=user,
        favorite_city="Madrid",
    )
