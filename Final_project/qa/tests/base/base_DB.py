import pytest

from functions import gen_rand_name, gen_rand_pass, gen_rand_email
from mysql_orm.models import TestUsers
from mysql_orm.mysql_orm_client import MysqlOrmConnection
from mysql_orm.orm_builder import MysqlOrmBuilder
from data.Data import *
from ui.fixtures_UI import registration_page


class DB:
    @pytest.fixture(scope='function', autouse=True)
    def setup_db(self, request):
        self.mysql: MysqlOrmConnection = request.getfixturevalue(
            'mysql_orm_client')
        self.builder = MysqlOrmBuilder(self.mysql)

    @pytest.fixture(scope="function")
    def add_del_valid_user(self):
        """Fixture to add valid user to DB, test and delete user"""

        user_data = {
            'u': gen_rand_name(),
            'p': gen_rand_pass(),
            'e': gen_rand_email()
        }
        self.add_user_for_test(user_data['u'], user_data['p'],
                               user_data['e'])
        yield user_data
        self.builder.del_user_by_name(user_data['u'])

    def add_user_for_test(self, username, password, email):
        self.builder.del_user_by_name(username)
        self.builder.del_user_by_name(email)
        self.builder.add_user(username, password, email)

    def registrate_user(self, registration_page, username, password, email):
        self.builder.del_user_by_name(username)
        self.builder.del_user_by_email(email)
        registration_page.registration(username, email, password,
                                       password, True)

    def check_different_username_to_registrate(self, registration_page,
                                               username):
        email = gen_rand_email()
        password = gen_rand_pass()
        self.registrate_user(registration_page, username=username,
                             password=password, email=email)
        try:
            check = registration_page.reg_is_complete()
            res = self.mysql.session.query(TestUsers).filter(
                TestUsers.username == username).first()
        finally:
            self.builder.del_user_by_name(username)
            self.builder.del_user_by_email(email)
        return check and res

    def check_different_email_to_registrate(self, registration_page,
                                            email):
        username = gen_rand_name()
        password = gen_rand_pass()
        self.registrate_user(registration_page, username=username,
                             password=password, email=email)
        try:
            check = registration_page.reg_is_complete()
            res = self.mysql.session.query(TestUsers).filter(
                TestUsers.username == username).first()
        finally:
            self.builder.del_user_by_name(username)
            self.builder.del_user_by_email(email)
        return check and res

    def check_different_password_to_registrate(self, registration_page,
                                               password):
        username = gen_rand_name()
        email = gen_rand_email()
        self.registrate_user(registration_page, username=username,
                             password=password, email=email)
        try:
            check = registration_page.reg_is_complete()
            res = self.mysql.session.query(TestUsers).filter(
                TestUsers.username == username).first()
        finally:
            self.builder.del_user_by_name(username)
            self.builder.del_user_by_email(email)
        return check and res
