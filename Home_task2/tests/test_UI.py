import pytest

from tests.base_UI import BaseCase


class Test(BaseCase):
    @pytest.mark.UI
    def test_authorization_success(self):
        self.authorization_page.authorization()
        check = self.authorization_page.find(
            self.authorization_page.locators.CHECK_AUTH_SUCCESS)
        assert check is not None

    @pytest.mark.UI
    def test_authorization_failed(self):
        self.authorization_page.authorization()
        

