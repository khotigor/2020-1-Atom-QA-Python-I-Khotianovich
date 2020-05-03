import pytest

from mysql_orm.mysql_orm_client import MysqlOrmConnection


@pytest.fixture(scope='session')
def mysql_orm_client():
    return MysqlOrmConnection('root', '', 'igor_test_db', '127.0.0.1', 3306)
