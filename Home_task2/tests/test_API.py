import random
import pytest

from api.Client import Client
from data.Data import EMAIL, PASSWORD

NAME_OF_SEGMENT_TO_ADD = "MySegmentFromAPI" + str(random.randint(0, 1000))
NAME_OF_SEGMENT_TO_DELETE = "MySegmentFromAPI" + str(random.randint(-1000, -1))


class Test:
    @pytest.fixture(scope='function')
    def api_client(self):
        user = EMAIL
        password = PASSWORD
        return Client(user, password)

    # def test_above_the_test_1(self, api_client):
    #     result = api_client.login()
    #     print(result)

    @pytest.mark.API
    def test_create_segment(self, api_client):
        assert api_client.create_segment(
            NAME_OF_SEGMENT_TO_ADD).status_code == 200

    @pytest.mark.API
    def test_delete_segment(self, api_client):
        assert api_client.delete_segment(
            api_client.create_segment(NAME_OF_SEGMENT_TO_ADD).json()['id']
        ).status_code == 204
