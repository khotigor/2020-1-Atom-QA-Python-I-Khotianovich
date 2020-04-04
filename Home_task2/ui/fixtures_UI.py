import os

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from ui.pages.AuthorizationPage import *
from data.Data import EMAIL, PASSWORD
from ui.pages.AuthorizedPage import AuthorizedPage


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


@pytest.fixture(scope="function")
def authorization(driver):
    page = AuthorizationPage(driver)
    page.authorization(EMAIL, PASSWORD)
    return AuthorizedPage(page.driver)


@pytest.fixture(scope="function")
def download_file():
    current_path = os.path.abspath(__file__)
    path = os.path.join(current_path, "..", "..", "data", "freddie.png")
    path = os.path.abspath(path)
    return path
