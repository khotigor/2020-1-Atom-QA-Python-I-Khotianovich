import pytest

from api.Client import Client
from data.Data import EMAIL, PASSWORD
from functions import create_name_of_segment


@pytest.fixture(scope="session")
def api_client():
    user = EMAIL
    password = PASSWORD
    return Client(user, password)


@pytest.fixture(scope='function')
def segment_request(api_client):
    name = create_name_of_segment('API', 0, 1000)
    request = api_client.create_segment(name)
    yield request
    api_client.delete_segment(request.json()['id'])
