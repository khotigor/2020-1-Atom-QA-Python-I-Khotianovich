import random
import time

from ui.pages.BasePage import BasePage
from ui.locators.locators_UI import CreateAdvertisingCampaignLocators

NAME_OF_CAMPAIGN = "I love Freddie" + str(random.randint(-1000, 1000))


class AuthorizedPage(BasePage):
    locators = CreateAdvertisingCampaignLocators()

    def create_campaign(self, file_to_download):

        try:
            self.click(self.locators.CREATE_ADVERTISING_CAMPAIGN_NOT_FIRST)
        except:
            self.click(self.locators.CREATE_ADVERTISING_CAMPAIGN)

        self.click(self.locators.TRAFFIC_TYPE_CAMPAIGN)
        self.input_data("mail.ru", self.locators.LINK_EDIT)
        self.input_data(NAME_OF_CAMPAIGN, self.locators.NAME_EDIT)
        self.click(self.locators.BANNER)
        download_pic = self.find(self.locators.DOWNLOAD)
        download_pic.send_keys(file_to_download)
        self.click(self.locators.BUTTON_CREATE)
        time.sleep(3)
        return self.find(self.locators.CHECK).get_attribute(
            'title') == NAME_OF_CAMPAIGN
