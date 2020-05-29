import pytest

from mysql_orm.mysql_orm_client import MysqlOrmConnection
from mysql_orm.orm_builder import MysqlOrmBuilder


@pytest.fixture(scope='function', autouse=True)
def setup(self, mysql_orm_client):
    self.mysql: MysqlOrmConnection = mysql_orm_client
    self.builder = MysqlOrmBuilder(mysql_orm_client)