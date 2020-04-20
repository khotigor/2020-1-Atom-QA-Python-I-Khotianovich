import pytest

from api.Client import Client
from data.Data import EMAIL, PASSWORD


@pytest.fixture(scope="session")
def api_client():
    user = EMAIL
    password = PASSWORD
    return Client(user, password)
