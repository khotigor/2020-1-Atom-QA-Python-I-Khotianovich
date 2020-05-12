import pytest

from functions import create_name_of_segment
from tests.base_UI import BaseCase
from data.Data import EMAIL, PASSWORD


class Test(BaseCase):
    @pytest.mark.UI
    def test_authorization_success(self):
        self.authorization_page.authorize(EMAIL, PASSWORD)
        check = self.authorization_page.find(
            self.authorization_page.locators.CHECK_AUTH_SUCCESS)
        assert check is not None, 'Authorization failed'

    @pytest.mark.UI
    def test_authorization_failed(self):
        self.authorization_page.authorize(EMAIL, "PASSWORD")
        check = self.authorization_page.find(
            self.authorization_page.locators.CHECK_AUTH_FAILED)
        assert check is not None, 'Authorization done, but has not'

    @pytest.mark.UI
    def test_create_advertising_campaign(self, advertising_campaign_request):
        assert advertising_campaign_request, \
            'Failed to create advertising campaign'

    @pytest.mark.UI
    def test_create_segment(self, create_segment_request):
        assert create_segment_request, 'Failed to create segment'

    @pytest.mark.UI
    def test_delete_segment(self, authorized_page):
        self.authorized_page = authorized_page
        name = create_name_of_segment('UI', -1000, -1)
        self.authorized_page.create_segment(name)
        assert self.authorized_page.delete_segment(name) is None, \
            'Failed to delete segment'
