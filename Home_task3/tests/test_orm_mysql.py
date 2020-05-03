import pytest

from mysql_orm.orm_builder import MysqlOrmBuilder
from mysql_orm.mysql_orm_client import MysqlOrmConnection
from python_parser.log_parser import Parser


class TestOrmMysql:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_orm_client):
        self.mysql: MysqlOrmConnection = mysql_orm_client
        """input path"""
        path = '/Users/igorkhotyanovich/projects/2020-1-Atom-QA-Python-I-Khotianovich/Home_task3/data'
        parser = Parser(path=path, json=False)
        self.builder = MysqlOrmBuilder(mysql_orm_client, parser=parser)

    @pytest.mark.db_log
    def test_a(self):
        self.builder.add_a()

    @pytest.mark.db_log
    def test_b(self):
        self.builder.add_b()

    @pytest.mark.db_log
    def test_c(self):
        self.builder.add_c()

    @pytest.mark.db_log
    def test_d(self):
        self.builder.add_d()

    @pytest.mark.db_log
    def test_e(self):
        self.builder.add_e()
