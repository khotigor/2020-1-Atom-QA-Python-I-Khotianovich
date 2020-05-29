from ui.locators.locators_UI import RegLocators
from ui.pages.BasePage import BasePage


class RegistrationPage(BasePage):
    locators = RegLocators()

    def find_user(self):
        user = self.find(self.locators.USERNAME_FIELD)
        return user

    def registration(self, user, email, password, password_conf, accept):
        user_field = self.find(self.locators.USERNAME_FIELD)
        user_field.clear()
        email_field = self.find(self.locators.EMAIL_FIELD)
        email_field.clear()
        password_field = self.find(self.locators.PASSWORD_FIELD)
        password_field.clear()
        password_conf_field = self.find(self.locators.PASSWORD_CONF_FIELD)
        password_conf_field.clear()

        user_field.send_keys(user)
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_conf_field.send_keys(password_conf)

        if accept:
            self.click(self.locators.TERM)

        self.click(self.locators.REG_BUTTON)

    def reg_is_complete(self):
        return self.find(self.locators.LOGOUT_BUTTON)

    def go_reg_again(self):
        self.click(self.locators.LOGOUT_BUTTON)
        self.click(self.locators.REGISTRATION)

    def find_vk_id(self):
        return self.find(self.locators.VK_ID)
