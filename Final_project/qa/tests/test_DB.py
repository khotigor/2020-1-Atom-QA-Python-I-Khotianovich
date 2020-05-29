import pytest

from mysql_orm.models import TestUsers
from tests.base.base_DB import DB


class TestDB(DB):

    @pytest.mark.DB
    def test_add_user_to_db(self, add_del_valid_user):
        """
        Test, that DB works normally.
        """
        res = self.mysql.session.query(TestUsers).filter(
            TestUsers.username == add_del_valid_user['u']).first()
        assert res is not None, 'Cant add user to DB directly'

    @pytest.mark.DB
    def test_where_is_md5(self, add_del_valid_user):
        """
        Passwords should be encrypted
        """
        res = self.mysql.session.query(TestUsers).filter(
            TestUsers.email == add_del_valid_user['e']).first().password
        print(res)

        assert res != add_del_valid_user['p'], \
            'Passwords in DB should be encrypted (use MD5)'
