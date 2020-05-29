import pytest

from functions import gen_rand_name, gen_rand_pass, gen_rand_email, \
    add_user_vk_id
from mysql_orm.models import TestUsers
from tests.base.base_DB import DB
from data.Data import *
from tests.base.base_UI import BaseCase


class TestUI(BaseCase, DB):

    @pytest.mark.UI
    def test_authorization_success(self, add_del_valid_user):
        """
        Check authorization.
        """
        self.authorization_page.authorize(add_del_valid_user['u'],
                                          add_del_valid_user['p'])
        check = self.authorization_page.find(
            self.authorization_page.locators.CHECK_AUTH_SUCCESS)
        assert check is not None, 'Authorization failed'

    @pytest.mark.UI
    def test_authorization_failed(self, add_del_valid_user):
        """
        Check authorization failed with wrong data.
        """
        self.authorization_page.authorize(add_del_valid_user['u'], 'PASSWORD')
        check = self.authorization_page.find(
            self.authorization_page.locators.CHECK_AUTH_FAILED)
        assert check is not None, 'Authorization done, but has not'

    @pytest.mark.UI
    def test_logout(self, authorized_page):
        """
        Check logout button.
        """
        authorized_page.logout()
        check = authorized_page.find(
            authorized_page.locators.FULL_PENETRATION_BUTTON)
        assert check is not None, 'Logout not done'

    @pytest.mark.UI
    def test_vk_id(self, registration_page):
        """
        Check active in DB after redirect after reg.
        """
        username = gen_rand_name()
        password = gen_rand_pass()
        add_user_vk_id(100, username)
        registration_page.registration(username, gen_rand_email(),
                                       password, password, True)
        check = registration_page.find_vk_id()
        self.builder.del_user_by_name(username)
        assert check is not None, \
            'Not active, but not passive'

    @pytest.mark.UI
    def test_active_after_reg(self, registration_page):
        """
        Check active in DB after redirect after reg.
        """
        username = gen_rand_name()
        password = gen_rand_pass()
        registration_page.registration(username, gen_rand_email(),
                                       password, password, True)
        check = registration_page.reg_is_complete()
        res_active = self.mysql.session.query(TestUsers).filter(
            TestUsers.username == username).first().active
        self.builder.del_user_by_name(username)
        assert check is not None and res_active == 1, \
            'Not active, but not passive'

    @pytest.mark.UI
    def test_active_after_logout(self, add_del_valid_user):
        """
        Check active in DB after login.
        """
        self.authorization_page.authorize(add_del_valid_user['u'],
                                          add_del_valid_user['p'])
        self.authorization_page.logout()
        res_active = self.mysql.session.query(TestUsers).filter(
            TestUsers.username == add_del_valid_user['u']).first().active
        assert res_active == 0, 'Not passive, but not active'

    @pytest.mark.UI
    def test_fact(self, authorized_page):
        """
        Check fact is on the page.
        """
        assert authorized_page.find_fact(), 'Cant find a fact'

    @pytest.mark.UI
    def test_home(self, authorized_page):
        """
        Check home button.
        """
        assert authorized_page.click_home(), 'Cant put home'

    @pytest.mark.UI
    def test_api(self, authorized_page):
        """
        Check api button.
        """
        assert authorized_page.click_api(), 'Cant put api'

    @pytest.mark.UI
    def test_future_int(self, authorized_page):
        """
        Check api button.
        """
        assert authorized_page.click_future_internet(), 'Cant put future int'

    @pytest.mark.UI
    def test_smtp(self, authorized_page):
        """
        Check smtp button.
        """
        assert authorized_page.click_smtp(), 'Cant put smpp'

    @pytest.mark.UI
    def test_pip_history(self, authorized_page):
        """
        Check python history button.
        """
        assert authorized_page.click_python_history(), \
            'Cant put python history'

    @pytest.mark.UI
    def test_pip(self, authorized_page):
        """
        Check python button.
        """
        assert authorized_page.click_python(), 'Cant put pip'

    @pytest.mark.UI
    def test_pip_flask(self, authorized_page):
        """
        Check python flask button.
        """
        assert authorized_page.click_python_flask(), 'Cant put pip flask'

    @pytest.mark.UI
    def test_cent_os_download(self, authorized_page):
        """
        Check cent os button.
        """
        assert authorized_page.click_cent_os(), 'Cant put cent os'

    @pytest.mark.UI
    def test_net_news(self, authorized_page):
        """
        Check net news button.
        """
        assert authorized_page.click_net_news(), 'Cant put net nes'

    @pytest.mark.UI
    def test_net_down(self, authorized_page):
        """
        Check net download button.
        """
        assert authorized_page.click_net_down(), 'Cant put net download'

    @pytest.mark.UI
    def test_net_example(self, authorized_page):
        """
        Check net download button.
        """
        assert authorized_page.click_net_example(), 'Cant put net example'

    @pytest.mark.UI
    def test_go_reg(self):
        """
        Check Create an registration url.
        """
        check = self.authorization_page.go_registration()
        assert check is not None, 'Registration url is bad'

    @pytest.mark.UI
    def test_valid_reg(self, registration_page, add_del_valid_user):
        """
        Check registration with valid data
        """
        username = gen_rand_name()
        password = gen_rand_pass()
        registration_page.registration(username, gen_rand_email(),
                                       password, password, True)
        check = registration_page.reg_is_complete()
        self.builder.del_user_by_name(username)
        assert check is not None, 'Cant registrate with valid data'

    @pytest.mark.UI
    def test_invalid_reg_no_accept(self, registration_page):
        """
        Check registration without accept that I want to be a SDET
        """
        username = gen_rand_name()
        password = gen_rand_pass()
        registration_page.registration(username, gen_rand_email(),
                                       password, password, False)
        check = registration_page.reg_is_complete()
        self.builder.del_user_by_name(username)
        assert check is None and check is None, \
            'Can registrate without accept terms'

    @pytest.mark.UI
    def test_invalid_reg_diff_pass(self, registration_page):
        """
        Check registration with different passwords
        """
        username = gen_rand_name()
        registration_page.registration(username, gen_rand_email(),
                                       gen_rand_pass(), gen_rand_pass(), True)
        check = registration_page.reg_is_complete()
        self.builder.del_user_by_name(username)
        assert check is None and check is None, \
            'Can registrate with different passwords'

    @pytest.mark.UI
    def test_invalid_reg_bad_username_1(self, registration_page):
        """
        Check registration with bad username. Bad chars in username.
        """
        self.builder.del_user_by_name(USER_BAD1)
        assert self.check_different_username_to_registrate(
            registration_page, USER_BAD1) is None, \
            'Can registrate with username with bad chars'

    @pytest.mark.UI
    def test_invalid_reg_bad_username_2(self, registration_page):
        """
        Check registration with bad username. Username is too short (one char).
        """
        assert self.check_different_username_to_registrate(
            registration_page, USER_BAD2) is None, \
            'Can registrate with username of one char'

    @pytest.mark.UI
    def test_invalid_reg_bad_username_3(self, registration_page):
        """
        Check registration with bad username. Username is a number).
        """
        assert self.check_different_username_to_registrate(
            registration_page, USER_BAD3) is None, \
            'Can registrate with username of number'

    @pytest.mark.UI
    def test_invalid_reg_bad_username_4(self, registration_page):
        """
        Check registration with same username
        """
        USER = gen_rand_name()
        PASSWORD = gen_rand_pass()
        EMAIL1 = gen_rand_email()
        EMAIL2 = gen_rand_email()

        self.builder.del_user_by_email(EMAIL1)
        self.builder.del_user_by_email(EMAIL2)

        registration_page.registration(USER, EMAIL1, PASSWORD,
                                       PASSWORD, True)
        registration_page.go_reg_again()
        registration_page.registration(USER, EMAIL2, PASSWORD,
                                       PASSWORD, True)
        check = registration_page.reg_is_complete()
        self.builder.del_user_by_name(USER)
        assert check is None, 'Can registrate with the same username'

    @pytest.mark.UI
    def test_invalid_reg_bad_email_1(self, registration_page):
        """
        Check registration with bad email.
        """
        assert self.check_different_email_to_registrate(
            registration_page, EMAIL_BAD1) is None, \
            'Can registrate with bad email: {e}'.format(e=EMAIL_BAD1)

    @pytest.mark.UI
    def test_invalid_reg_bad_email_2(self, registration_page):
        """
        Check registration with bad email.
        """
        assert self.check_different_email_to_registrate(
            registration_page, EMAIL_BAD2) is None, \
            'Can registrate with bad email: {e}'.format(e=EMAIL_BAD2)

    @pytest.mark.UI
    def test_invalid_reg_bad_email_3(self, registration_page):
        """
        Check registration with bad email.
        """
        assert self.check_different_email_to_registrate(
            registration_page, EMAIL_BAD3) is None, \
            'Can registrate with bad email: {e}'.format(e=EMAIL_BAD3)

    @pytest.mark.UI
    def test_invalid_reg_bad_email_1(self, registration_page):
        """
        Check registration with bad password.
        """
        assert self.check_different_password_to_registrate(
            registration_page, PASSWORD_BAD1) is None, \
            'Can registrate with bad password: {e}'.format(e=PASSWORD_BAD1)

    @pytest.mark.UI
    def test_invalid_reg_bad_email_2(self, registration_page):
        """
        Check registration with bad password.
        """
        assert self.check_different_password_to_registrate(
            registration_page, PASSWORD_BAD2) is None, \
            'Can registrate with bad password: {e}'.format(e=PASSWORD_BAD2)

    @pytest.mark.UI
    def test_invalid_reg_bad_email_3(self, registration_page):
        """
        Check registration with bad password.
        """
        assert self.check_different_password_to_registrate(
            registration_page, PASSWORD_BAD2) is None, \
            'Can registrate with bad password: {e}'.format(e=PASSWORD_BAD3)

    @pytest.mark.UI
    def test_invalid_reg_bad_email_4(self, registration_page):
        """
        Check registration with the same email
        """
        USER1 = gen_rand_name()
        USER2 = gen_rand_name()

        PASSWORD = gen_rand_pass()
        EMAIL = gen_rand_email()

        self.builder.del_user_by_name(USER1)
        self.builder.del_user_by_email(USER2)
        self.builder.del_user_by_email(EMAIL)

        registration_page.registration(USER1, EMAIL, PASSWORD,
                                       PASSWORD, True)
        registration_page.go_reg_again()
        registration_page.registration(USER2, EMAIL, PASSWORD,
                                       PASSWORD, True)
        check = registration_page.reg_is_complete()
        self.builder.del_user_by_name(USER1)
        self.builder.del_user_by_name(USER2)
        assert check is None, 'Can registrate with the same email'
