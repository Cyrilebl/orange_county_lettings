from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents an address associated with a letting.

    Attributes:
        number (PositiveIntegerField): The street number (up to 99999).
        street (CharField): The name of the street.
        city (CharField): The city in which the address is located.
        state (CharField): The state consisting of 2 characters.
        zip_code (PositiveIntegerField): The postal code (up to 99999).
        country_iso_code (CharField): The iso code for the country (3 characters).

    Methods:
        __str__: Returns a string representation of the address.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        return f"{self.number} {self.street}"

    class Meta:
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Represents a rental letting linked to an address.

    Attributes:
        title (CharField): The title of the rental letting (up to 256 characters).
        address (OneToOneField): A one-to-one relationship with the Address model.

    Methods:
        __str__: Returns the title of the letting.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
