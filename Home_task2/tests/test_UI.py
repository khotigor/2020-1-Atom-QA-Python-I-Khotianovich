import pytest

from functions import create_name_of_segment
from tests.base_UI import BaseCase
from data.Data import EMAIL, PASSWORD
import random

NAME_OF_CAMPAIGN = "I love Freddie" + str(random.randint(-1000, 1000))


class Test(BaseCase):
    @pytest.mark.UI
    def test_authorization_success(self):
        self.authorization_page.authorize(EMAIL, PASSWORD)
        check = self.authorization_page.find(
            self.authorization_page.locators.CHECK_AUTH_SUCCESS)
        assert check is not None

    @pytest.mark.UI
    def test_authorization_failed(self):
        self.authorization_page.authorize(EMAIL, "PASSWORD")
        check = self.authorization_page.find(
            self.authorization_page.locators.CHECK_AUTH_FAILED)
        assert check is not None

    @pytest.mark.UI
    def test_create_advertising_campaign(self, authorized_page, download_file):
        self.authorized_page = authorized_page
        res = self.authorized_page.create_campaign(download_file,
                                                   NAME_OF_CAMPAIGN)
        self.authorized_page.delete_campaign(NAME_OF_CAMPAIGN)
        assert res

    @pytest.mark.UI
    def test_create_segment(self, authorized_page):
        self.authorized_page = authorized_page
        name = create_name_of_segment('UI', 0, 1000)
        res = self.authorized_page.create_segment(name)
        self.authorized_page.delete_segment(name)
        assert res

    @pytest.mark.UI
    def test_delete_segment(self, authorized_page):
        self.authorized_page = authorized_page
        name = create_name_of_segment('UI', -1000, -1)
        self.authorized_page.create_segment(name)
        assert self.authorized_page.delete_segment(name)
