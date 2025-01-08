import pytest
from django.test import Client
from django.urls import reverse


@pytest.fixture
def client() -> Client:
    """Fixture for Django test client."""
    return Client()


@pytest.fixture
def sample_contact_data():
    """Fixture for valid contact data."""
    return {
        "name": "Test User",
        "email": "testuser@example.com",
        "subject": "Test Subject",
        "message": "Test Message",
    }


@pytest.fixture
def contact_url():
    """Fixture for the contact view URL."""
    return reverse('contact')
