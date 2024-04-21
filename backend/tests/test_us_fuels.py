import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db(transaction=True)
def test_offer_export_view():
    client = APIClient()
    response = client.get('/api/fuels/export/')
    assert response.status_code == 200, 'Статус ответа не равен 200'