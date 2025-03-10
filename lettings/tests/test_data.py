from lettings.models import Address, Letting


def create_address():
    """
    Create and return an Address instance.
    """
    return Address.objects.create(
        number="123",
        street="Main Street",
        city="New York",
        state="NY",
        zip_code="10001",
        country_iso_code="USA",
    )


def create_letting(address):
    """
    Create and return a Letting instance linked to a given Address.
    """
    return Letting.objects.create(
        title="test",
        address=address,
    )
