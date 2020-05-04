import pytest
import requests

from mysql_orm.mysql_orm_client import MysqlOrmConnection
from my_mock import mock


@pytest.fixture(scope='session')
def mysql_orm_client():
    return MysqlOrmConnection('root', '', 'igor_test_db', '127.0.0.1', 3306)


@pytest.fixture(scope='session')
def mock_server():
    server = mock.run_mock()
    server_host = server._kwargs['host']
    server_port = server._kwargs['port']

    yield server_host, server_port

    shutdown_url = f'http://{server_host}:{server_port}/shutdown'
    requests.get(shutdown_url)
