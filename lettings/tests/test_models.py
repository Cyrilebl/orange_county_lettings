from django.test import TestCase
from .test_data import create_address, create_letting


class AddressTest(TestCase):
    def test_create_model(self):
        """
        Test the creation of an Address instance.
        """
        address = create_address()
        self.assertEqual(address.city, "New York")


class LettingTest(TestCase):
    def test_create_model(self):
        """
        Test the creation of a Letting instance.
        """
        address = create_address()
        letting = create_letting(address)

        self.assertEqual(letting.title, "test")
