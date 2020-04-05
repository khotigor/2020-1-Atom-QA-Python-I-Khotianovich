import pytest
from tests.base_UI import BaseCase
from data.Data import EMAIL, PASSWORD


class Test(BaseCase):
    @pytest.mark.UI
    def test_authorization_success(self):
        self.authorization_page.authorization(EMAIL, PASSWORD)
        check = self.authorization_page.find(
            self.authorization_page.locators.CHECK_AUTH_SUCCESS)
        assert check is not None

    @pytest.mark.UI
    def test_authorization_failed(self):
        self.authorization_page.authorization(EMAIL, "PASSWORD")
        check = self.authorization_page.find(
            self.authorization_page.locators.CHECK_AUTH_FAILED)
        assert check is not None

    @pytest.mark.UI
    def test_create_advertising_campaign(self, authorization, download_file):
        self.authorized_page = authorization
        assert self.authorized_page.create_campaign(download_file)

    @pytest.mark.UI
    def test_create_segment(self, authorization,
                            create_name_of_segment_for_add):
        self.authorized_page = authorization
        assert self.authorized_page.create_segment(
            create_name_of_segment_for_add)

    @pytest.mark.UI
    def test_delete_segment(self, authorization,
                            create_name_of_segment_for_delete):
        self.authorized_page = authorization
        name = create_name_of_segment_for_delete
        self.authorized_page.create_segment(name)
        assert self.authorized_page.delete_segment(name)
