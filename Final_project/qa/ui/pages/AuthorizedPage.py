import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from ui.pages.BasePage import BasePage
from ui.locators.locators_UI import LogOutLocators, AuthorizedPageLocators


class SiteHasChanged(Exception):
    pass


class AuthorizedPage(BasePage):
    locators = AuthorizedPageLocators()

    def logout(self):
        self.click(self.locators.LOGOUT_BUTTON)
        return self.find(self.locators.FULL_PENETRATION_BUTTON)

    def find_fact(self):
        return self.find(self.locators.FACT)

    def click_home(self):
        self.click(self.locators.HOME_BUTTON)
        return self.find(self.locators.FACT)

    def click_api(self):
        self.click(self.locators.PICTURE_ONE_BUTTON)
        self.driver.switch_to_window(self.driver.window_handles[1])
        return self.driver.current_url == \
               'https://en.wikipedia.org/wiki/Application_programming_interface'

    def click_future_internet(self):
        self.click(self.locators.PICTURE_TWO_BUTTON)
        self.driver.switch_to_window(self.driver.window_handles[1])
        return self.driver.current_url == \
               'https://www.popularmechanics.com/technology/infrastructure/a29666802/future-of-the-internet/'

    def click_smtp(self):
        self.click(self.locators.PICTURE_THREE_BUTTON)
        self.driver.switch_to_window(self.driver.window_handles[1])
        return self.driver.current_url == \
               'https://ru.wikipedia.org/wiki/SMTP'

    def click_python_history(self):
        ac_python = ActionChains(self.driver)
        ac_python.move_to_element(
            self.find(self.locators.PYTHON_BUTTON)).perform()
        self.click(self.locators.PYTHON_HISTORY)
        return self.driver.current_url == \
               'https://en.wikipedia.org/wiki/History_of_Python'

    def click_python(self):
        self.click(self.locators.PYTHON_BUTTON)
        return self.driver.current_url == \
               'https://www.python.org/'

    def click_python_flask(self):
        ac_flask = ActionChains(self.driver)
        ac_flask.move_to_element(
            self.find(self.locators.PYTHON_BUTTON)).perform()
        self.click(self.locators.FLASK_BUTTON)
        self.driver.switch_to_window(self.driver.window_handles[1])
        return self.driver.current_url == \
               'https://flask.palletsprojects.com/en/1.1.x/#'

    def click_cent_os(self):
        ac_cent = ActionChains(self.driver)
        ac_cent.move_to_element(
            self.find(self.locators.LINUX_BUTTON)).perform()
        self.click(self.locators.DOWNLOAD_CENT_OS)
        self.driver.switch_to_window(self.driver.window_handles[1])
        return self.driver.current_url == \
               'https://wiki.centos.org/Download'

    def click_net_news(self):
        ac_net_news = ActionChains(self.driver)
        ac_net_news.move_to_element(
            self.find(self.locators.NETWORK_BUTTON)).perform()
        self.click(self.locators.NETWORK_NEWS)
        self.driver.switch_to_window(self.driver.window_handles[1])
        return self.driver.current_url == \
               'https://www.wireshark.org/news/'

    def click_net_down(self):
        ac_net_down = ActionChains(self.driver)
        ac_net_down.move_to_element(
            self.find(self.locators.NETWORK_BUTTON)).perform()
        self.click(self.locators.NETWORK_DOWNLOAD)
        self.driver.switch_to_window(self.driver.window_handles[1])
        return self.driver.current_url == \
               'https://www.wireshark.org/#download'

    def click_net_example(self):
        ac_net_ex = ActionChains(self.driver)
        ac_net_ex.move_to_element(
            self.find(self.locators.NETWORK_BUTTON)).perform()
        self.click(self.locators.NETWORK_EXAMPLE)
        self.driver.switch_to_window(self.driver.window_handles[1])
        return self.driver.current_url == \
               'https://hackertarget.com/tcpdump-examples/'
