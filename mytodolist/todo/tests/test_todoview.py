import pytest
from django.test import Client


@pytest.mark.django_db
def test_status_code(client: Client):
    resp = client.get('/todo/')
    assert resp.status_code == 200
