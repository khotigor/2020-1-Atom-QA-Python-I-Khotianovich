from selenium.webdriver.common.keys import Keys

from ui.pages.BasePage import BasePage
from data.Data import *
from ui.locators.locators_UI import AuthorizationLocators


class AuthorizationPage(BasePage):
    locators = AuthorizationLocators()

    def authorization(self):
        self.click(self.locators.FULL_PENETRATION_BUTTON)
        email_field = self.find(self.locators.EMAIL_FIELD)
        password_field = self.find(self.locators.PASSWORD_FIELD)
        email_field.clear()
        password_field.clear()
        email_field.send_keys(EMAIL)
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.RETURN)
