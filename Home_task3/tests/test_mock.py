import time

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

    def test_http_client_get(self, mock_server, http_client):
        user = {'name': 'Ilya', 'surname': 'Kirillov'}
        add_user(1, user)
        res = http_client.get_user('/user/1')
        assert res['user'] == user

    # def test_http_client_post(self, mock_server, http_client):
    #     user = {'name': 'Ilya2', 'surname': 'Kirillov2'}
    #     http_client.post_user(user)
    #     res = http_client.get_user('/user')
    #     assert res['user'] == user
