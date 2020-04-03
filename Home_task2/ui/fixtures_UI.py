import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from ui.pages.AuthorizationPage import AuthorizationPage


class NotChrome(Exception):
    pass


@pytest.fixture(scope="function")
def driver(config):
    browser = config["browser"]
    selenoid = config["selenoid"]
    url = config["url"]

    if browser == "chrome":
        if not selenoid:
            manager = ChromeDriverManager()
            driver = webdriver.Chrome(executable_path=manager.install())
        else:
            cap = {"browserName": browser, "version": "80.0"}
            options = webdriver.ChromeOptions()
            driver = webdriver.Remote(command_executor=selenoid,
                                      options=options,
                                      desired_capabilities=cap)
    else:
        raise NotChrome("Sorry, work only with chrome")
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.close()


@pytest.fixture(scope="function")
def authorization_page(driver):
    return AuthorizationPage(driver)
