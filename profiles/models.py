"""
Defines the database model for profiles.
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    This model represents a user profile, extending the default User model
    with additional information such as the user's favorite city.

    Methods:
        __str__: Returns the username of the associated User.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profiles")
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
