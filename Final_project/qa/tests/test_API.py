import pytest
from api.fixtures_API import *
from mysql_orm.models import TestUsers
from tests.base.base_DB import DB, USER_BAD2_API, USER_BAD1_API, USER_BAD3_API, \
    PASSWORD_BAD1_API, PASSWORD_BAD2_API, PASSWORD_BAD3_API, EMAIL_BAD1_API, \
    EMAIL_BAD2_API, EMAIL_BAD3_API
from functions import *

"""
Самые странные результаты тестов:
- Можно добавить юзера с коротким именем, хотя UI не позволяет. Видимо, зашито 
на front.
- Странное поведение при добавлении с существующим email. Возвращает 210, но 
не добавляет, в UI пишет 500.
- На некоторые плохие мыла выдает:
Object of type function is not JSON serializable
- GET /static/scripts/findMeError.js HTTP/1.1 ???
"""


class TestAPI(DB):

    @pytest.mark.API
    def test_login(self, api_client):
        """
        Test login by API.
        """
        username = gen_rand_name()
        self.add_user_for_test(username, gen_rand_pass(), gen_rand_email())
        check = api_client.login().status_code
        self.builder.del_user_by_name(username)
        assert check == 200, 'Cant login, status is not 200'

    @pytest.mark.API
    def test_add_user(self, api_client):
        """
        POST http://<APP_HOST>:<APP_PORT>/api/add_user
        Test adding user by API.
        """
        assert self.add_user(api_client, gen_rand_name(), gen_rand_pass(),
                             gen_rand_email()), \
            'Cant add user, status is not 201 or DB is bad'

    @pytest.mark.API
    def test_add_user_invalid_username1(self, api_client):
        """
        POST http://<APP_HOST>:<APP_PORT>/api/add_user
        Test adding user by API with bad username=USER_BAD_API1
        """

        assert not self.add_user(api_client, USER_BAD1_API, gen_rand_pass(),
                                 gen_rand_email()), \
            'Can add user username={u}'.format(u=USER_BAD1_API)

    @pytest.mark.API
    def test_add_user_invalid_username2(self, api_client):
        """
        POST http://<APP_HOST>:<APP_PORT>/api/add_user
        Test adding user by API with bad username=USER_BAD_API2
        """

        assert not self.add_user(api_client, USER_BAD2_API, gen_rand_pass(),
                                 gen_rand_email()), \
            'Can add user username={u}'.format(u=USER_BAD2_API)

    @pytest.mark.API
    def test_add_user_invalid_username3(self, api_client):
        """
        POST http://<APP_HOST>:<APP_PORT>/api/add_user
        Test adding user by API with bad username=USER_BAD_API1
        """

        assert not self.add_user(api_client, USER_BAD3_API, gen_rand_pass(),
                                 gen_rand_email()), \
            'Can add user username={u}'.format(u=USER_BAD3_API)

    @pytest.mark.API
    def test_add_user_invalid_pass1(self, api_client):
        """
        POST http://<APP_HOST>:<APP_PORT>/api/add_user
        Test adding user by API with bad password=PASSWORD_BAD1_API
        """

        assert not self.add_user(api_client, gen_rand_name(),
                                 PASSWORD_BAD1_API,
                                 gen_rand_email()), \
            'Can add user password={p}'.format(p=PASSWORD_BAD1_API)

    @pytest.mark.API
    def test_add_user_invalid_pass2(self, api_client):
        """
        POST http://<APP_HOST>:<APP_PORT>/api/add_user
        Test adding user by API with bad password=PASSWORD_BAD2_API
        """

        assert not self.add_user(api_client, gen_rand_name(),
                                 PASSWORD_BAD2_API,
                                 gen_rand_email()), \
            'Can add user password={p}'.format(p=PASSWORD_BAD2_API)

    @pytest.mark.API
    def test_add_user_invalid_pass3(self, api_client):
        """
        POST http://<APP_HOST>:<APP_PORT>/api/add_user
        Test adding user by API with bad password=PASSWORD_BAD3_API
        """

        assert not self.add_user(api_client, gen_rand_name(),
                                 PASSWORD_BAD2_API,
                                 gen_rand_email()), \
            'Can add user password={p}'.format(p=PASSWORD_BAD2_API)

    @pytest.mark.API
    def test_add_user_invalid_email1(self, api_client):
        """
        POST http://<APP_HOST>:<APP_PORT>/api/add_user
        Test adding user by API with bad password=EMAIL_BAD1_API
        """

        assert not self.add_user(api_client, gen_rand_name(),
                                 gen_rand_pass(),
                                 EMAIL_BAD1_API), \
            'Can add user email={e}'.format(e=EMAIL_BAD1_API)

    @pytest.mark.API
    def test_add_user_invalid_email2(self, api_client):
        """
        POST http://<APP_HOST>:<APP_PORT>/api/add_user
        Test adding user by API with bad password=EMAIL_BAD2_API
        """

        assert not self.add_user(api_client, gen_rand_name(),
                                 gen_rand_pass,
                                 EMAIL_BAD2_API), \
            'Can add user email={e}'.format(e=EMAIL_BAD2_API)

    @pytest.mark.API
    def test_add_user_invalid_email3(self, api_client):
        """
        POST http://<APP_HOST>:<APP_PORT>/api/add_user
        Test adding user by API with bad password=EMAIL_BAD3_API
        """

        assert not self.add_user(api_client, gen_rand_name(),
                                 gen_rand_pass,
                                 EMAIL_BAD3_API), \
            'Can add user email={e}'.format(e=EMAIL_BAD3_API)

    @pytest.mark.API
    def test_add_user_same_name(self, api_client):
        """
        POST http://<APP_HOST>:<APP_PORT>/api/add_user
        Test adding user with not uniq name by API.
        """
        username_to_add = gen_rand_name()
        password_to_add = gen_rand_pass()
        email_to_add = gen_rand_email()
        email_to_add2 = gen_rand_email()

        api_client.login()
        self.builder.del_user_by_name(username_to_add)
        self.builder.del_user_by_email(email_to_add)
        check_add = api_client.add_user(username_to_add, password_to_add,
                                        email_to_add).status_code
        check_add_again = api_client.add_user(username_to_add, password_to_add,
                                              email_to_add2).status_code

        self.builder.del_user_by_name(username_to_add)
        assert check_add_again == 304, \
            'Can add user with not uniq name, status code is not 304'

    @pytest.mark.API
    def test_add_user_same_email(self, api_client):
        """
        POST http://<APP_HOST>:<APP_PORT>/api/add_user
        Test adding user not uniq email by API.
        """
        username_to_add = gen_rand_name()
        username_to_add2 = gen_rand_name()

        password_to_add = gen_rand_pass()
        email_to_add = gen_rand_email()

        api_client.login()
        self.builder.del_user_by_name(username_to_add)
        self.builder.del_user_by_email(email_to_add)
        check_add = api_client.add_user(username_to_add, password_to_add,
                                        email_to_add).status_code
        check_add_ag = api_client.add_user(username_to_add2, password_to_add,
                                           email_to_add).status_code

        self.builder.del_user_by_email(email_to_add)
        assert check_add_ag == 304, \
            'Can add user with not uniq email, status code is not 304'

    @pytest.mark.API
    def test_del_user(self, api_client):
        """
        GET http://<APP_HOST>:<APP_PORT>/api/del_user/<username>
        Check delete user by API.
        """
        username = gen_rand_name()
        self.add_user_for_test(username, gen_rand_pass(), gen_rand_email())
        api_client.login()
        check = api_client.del_user(username).status_code
        res = self.mysql.session.query(TestUsers).filter(
            TestUsers.username == username).first()
        self.builder.del_user_by_name(username)
        assert check == 204 and res is None, \
            'Cant delete user, status code is not 200 or 204'

    @pytest.mark.API
    def test_block_user(self, api_client):
        """
        GET http://<APP_HOST>:<APP_PORT>/api/block_user/<username>
        Block user by API.
        """
        username = gen_rand_name()
        password = gen_rand_pass()
        self.add_user_for_test(username, password, gen_rand_email())
        api_client.login()
        check_code_block = api_client.block_user(username).status_code
        res = self.mysql.session.query(TestUsers).filter(
            TestUsers.username == username).first().access
        check_code_login = api_client.login_dif_user(username,
                                                     password).status_code
        self.builder.del_user_by_name(username)
        assert check_code_block == 200 and res == 0 \
               and check_code_login == 401, \
            'Cant block user, status code is not 200 or DB data is bad'

    @pytest.mark.API
    def test_unblock_user(self, api_client):
        """
        Check GET http://<APP_HOST>:<APP_PORT>/api/accept_user/<username>
        Unblock user by API.
        """
        username = gen_rand_name()
        password = gen_rand_pass()
        self.add_user_for_test(username, password, gen_rand_email())
        api_client.login()
        check_code_block = api_client.block_user(username).status_code
        check_code_unblock = api_client.unblock_user(username).status_code
        res = self.mysql.session.query(TestUsers).filter(
            TestUsers.username == username).first().access
        check_code_login = api_client.login_dif_user(username,
                                                     password).status_code
        self.builder.del_user_by_name(username)
        assert check_code_block == check_code_unblock == 200 and res == 1 and \
               check_code_login == 200, \
            'Cant unblock user, status code is not 200 or DB data is bad'

    @pytest.mark.API
    def test_status_of_application(self, api_client):
        """
        Check GET http://<APP_HOST>:<APP_PORT>/status
        Get status of application by API.
        """
        check_code = api_client.get_status_of_app().status_code
        check_json = api_client.get_status_of_app().json()
        assert check_code == 200 and check_json == {"status": "ok"}, \
            'Is app norm?'

    @pytest.mark.API
    def test_bad_request(self, api_client):
        """
        Check GET http://<APP_HOST>:<APP_PORT>/<bad>
        Get bad request by API.
        """
        check_code = api_client.dump_req().status_code
        assert check_code == 400 or check_code == 404, \
            'Can send a rubbish'

    @pytest.mark.API
    def test_bad_request(self, api_client):
        """
        Check GET http://<APP_HOST>:<APP_PORT>/<bad>
        Get bad request by API.
        """
        check_code = api_client.dump_req().status_code
        assert check_code == 400 or check_code == 404, \
            'Can send a rubbish'

    @pytest.mark.API
    def test_find_me_error(self, api_client):
        """
        Check GET /static/scripts/findMeError.js HTTP/1.1
        Get bad request by API.
        """
        check_code = api_client.find_me_error().status_code
        assert check_code != 404, \
            'What the? very strange .js'

    """
    Useful functions
    """

    def add_user(self, api_client, username_to_add, password_to_add,
                 email_to_add):
        api_client.login()
        self.builder.del_user_by_name(username_to_add)
        self.builder.del_user_by_email(email_to_add)
        check = api_client.add_user(username_to_add, password_to_add,
                                    email_to_add).status_code
        res_em = self.mysql.session.query(TestUsers).filter(
            TestUsers.username == username_to_add).first().email
        res_user = self.mysql.session.query(TestUsers).filter(
            TestUsers.username == username_to_add).first().email
        self.builder.del_user_by_name(username_to_add)
        return res_em == email_to_add, res_user == username_to_add, \
               check == 201
