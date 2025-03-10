from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a user profile with an additional field for the user's favorite city.

    Attributes:
        user (OneToOneField): The user associated with the profile.
        favorite_city (CharField): The user's favorite city (optional, up to 64 characters).

    Methods:
        __str__: Returns the username of the associated User.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profiles")
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
