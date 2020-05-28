import pytest

from api.Client import Client


@pytest.fixture(scope="function")
def api_client(add_del_valid_user):
    user = add_del_valid_user['u']
    password = add_del_valid_user['p']
    return Client(user, password)


