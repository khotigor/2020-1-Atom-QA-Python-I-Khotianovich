import pytest
import requests

from api.Client import Client
from data.Data import EMAIL, PASSWORD


class Test:
    @pytest.fixture(scope='function')
    def api_client(self):
        user = EMAIL
        password = PASSWORD
        return Client(user, password)

    # def test(self, api_client):
    #     result = api_client.login()
    #     print(result)

    @pytest.mark.API
    def test_create_segment(self, api_client):
        assert api_client.create_segment().status_code == 200

