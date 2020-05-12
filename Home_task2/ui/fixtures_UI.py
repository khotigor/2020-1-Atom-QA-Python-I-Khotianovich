import os
import random

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from functions import create_name_of_segment
from ui.pages.AuthorizationPage import *
from data.Data import EMAIL, PASSWORD
from ui.pages.AuthorizedPage import AuthorizedPage
from selenium.webdriver import ChromeOptions


class NotChrome(Exception):
    pass


NAME_OF_CAMPAIGN = "I love Freddie" + str(random.randint(-1000, 1000))


@pytest.fixture(scope="function")
def driver(config):
    browser = config["browser"]
    version = config['version']
    selenoid = config["selenoid"]
    url = config["url"]

    if browser == "chrome":
        if not selenoid:
            manager = ChromeDriverManager(version=version)
            driver = webdriver.Chrome(executable_path=manager.install())
        else:
            options = ChromeOptions()
            capabilities = {'acceptInsecureCerts': True,
                            'browserName': 'chrome',
                            'version': '80.0',
                            }
            driver = webdriver.Remote(command_executor=selenoid,
                                      options=options,
                                      desired_capabilities=capabilities)
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
def authorized_page(driver):
    page = AuthorizationPage(driver)
    page.authorize(EMAIL, PASSWORD)
    return AuthorizedPage(page.driver)


@pytest.fixture(scope="function")
def download_file():
    current_path = os.path.abspath(__file__)
    path = os.path.join(current_path, "..", "..", "data", "freddie.png")
    path = os.path.abspath(path)
    return path


@pytest.fixture(scope='function')
def advertising_campaign_request(authorized_page, download_file):
    authorized_page = authorized_page
    yield authorized_page.create_campaign(download_file, NAME_OF_CAMPAIGN)
    authorized_page.delete_campaign(NAME_OF_CAMPAIGN)


@pytest.fixture(scope='function')
def create_segment_request(authorized_page):
    authorized_page = authorized_page
    name = create_name_of_segment('UI', 0, 1000)
    yield authorized_page.create_segment(name)
    authorized_page.delete_segment(name)
