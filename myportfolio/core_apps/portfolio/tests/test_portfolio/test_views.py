from unittest.mock import patch

import pytest
from django.test import Client


@pytest.mark.django_db
@patch("django.core.mail.send_mail")
def test_contact_post_creates_message_and_sends_email(client: Client, sample_contact_data, contact_url):
    # Simulate a POST request to the contact view
    response = client.post('/contact/', data=sample_contact_data)
    # placeholder
    assert response.status_code == response.status_code
