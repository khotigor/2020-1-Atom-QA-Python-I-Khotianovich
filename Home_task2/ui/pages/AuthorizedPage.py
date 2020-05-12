from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from ui.pages.BasePage import BasePage
from ui.locators.locators_UI import CreateAdvertisingCampaignLocators, \
    CreateSegmentLocators, DeleteSegmentLocators, \
    DeleteAdvertisingCampaignLocators


class SiteHasChanged(Exception):
    pass


class AuthorizedPage(BasePage):
    locatorsCAC = CreateAdvertisingCampaignLocators()
    locatorsDAC = DeleteAdvertisingCampaignLocators()
    locatorsCSL = CreateSegmentLocators()
    locatorsDSL = DeleteSegmentLocators()

    def create_campaign(self, file_to_download, name):

        try:
            self.click(self.locatorsCAC.CREATE_ADVERTISING_CAMPAIGN_NOT_FIRST)
        except:
            try:
                self.click(self.locatorsCAC.CREATE_ADVERTISING_CAMPAIGN)
            except:
                raise SiteHasChanged("Site has changed, update locators")

        self.click(self.locatorsCAC.TRAFFIC_TYPE_CAMPAIGN)
        self.input_data("mail.ru", self.locatorsCAC.LINK_EDIT)
        self.input_data(name, self.locatorsCAC.NAME_EDIT)
        self.click(self.locatorsCAC.BANNER)
        download_pic = self.find(self.locatorsCAC.DOWNLOAD)
        download_pic.send_keys(file_to_download)
        self.click(self.locatorsCAC.BUTTON_CREATE)
        return self.find(self.locatorsCAC.CHECK).get_attribute(
            'title') == name

    def delete_campaign(self, name):
        self.click(self.locatorsDAC.SEARCH)
        self.input_data(name, self.locatorsDAC.SEARCH)
        self.click(self.locatorsDAC.SUGGEST)
        self.click(self.locatorsDAC.SELECT_ALL)
        self.click(self.locatorsDAC.ACTION)
        self.click(self.locatorsDAC.DELETE)

    def create_segment(self, name):
        self.click(self.locatorsCSL.AUDITORIUMS)
        try:
            self.click(self.locatorsCSL.CREATE_SEGMENT_BUTTON_NOT_FIRST)
        except:
            try:
                self.click(self.locatorsCSL.CREATE_SEGMENT_BUTTON)
            except:
                raise SiteHasChanged("Site has changed, update locators")
        self.input_data(name, self.locatorsCSL.NAME_EDIT)
        self.click(self.locatorsCSL.ADD_AUDITORIUM_SEGMENT)
        self.click(self.locatorsCSL.PLAYED_CHOICE)
        self.click(self.locatorsCSL.PAYED_CHOICE)
        self.click(self.locatorsCSL.ADD_SEGMENT)
        self.click(self.locatorsCSL.CREATE_SEGMENT)
        check = (By.PARTIAL_LINK_TEXT, name)
        return self.find(check).is_displayed()

    def delete_segment(self, name):
        self.click(self.locatorsDSL.AUDITORIUMS)
        self.input_data(name, self.locatorsDSL.SEARCH_EDIT)
        search = self.find(self.locatorsDSL.SEARCH_EDIT)
        search.click()
        search.send_keys(Keys.ARROW_DOWN)
        search.send_keys(Keys.ENTER)
        self.click(self.locatorsDSL.CROSS)
        self.click(self.locatorsDSL.DELETE_BUTTON)
        self.click(self.locatorsDSL.AUDITORIUMS)
        check = (By.PARTIAL_LINK_TEXT, name)
        return self.find(check)
