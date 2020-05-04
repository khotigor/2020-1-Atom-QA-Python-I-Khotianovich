import pytest
import requests

from my_mock.mock import users


def add_user(user_id: int, user_data: dict):
    users.update({str(user_id): user_data})


@pytest.mark.mock
class TestMock:
    def test_valid_name(self, mock_server):
        server_host, server_port = mock_server

        user = {'name': 'Ilya', 'surname': 'Kirillov'}
        add_user(1, user)

        url = f'http://{server_host}:{server_port}/user/1'

        result = requests.get(url, user)
        assert result.json() == user
