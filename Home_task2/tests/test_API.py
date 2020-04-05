import pytest

from api.Client import Client
from data.Data import EMAIL, PASSWORD


class Test:
    @pytest.fixture(scope='function')
    def api_client(self):
        return Client()

    def test(self, api_client):
        print("Start")
        api_client.get_token()
