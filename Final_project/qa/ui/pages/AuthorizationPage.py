from selenium.webdriver.common.keys import Keys

from ui.pages.BasePage import BasePage
from ui.locators.locators_UI import AuthorizationLocators


class AuthorizationPage(BasePage):
    locators = AuthorizationLocators()

    def authorize(self, user, password):
        self.click(self.locators.FULL_PENETRATION_BUTTON)
        user_field = self.find(self.locators.USERNAME_FIELD)
        password_field = self.find(self.locators.PASSWORD_FIELD)
        user_field.clear()
        password_field.clear()
        user_field.send_keys(user)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

    def go_registration(self):
        self.click(self.locators.REGISTRATION)
        return self.find(self.locators.REGISTRATION_SUBMIT)

    def logout(self):
        self.click(self.locators.LOGOUT_BUTTON)
        return self.find(self.locators.FULL_PENETRATION_BUTTON)
