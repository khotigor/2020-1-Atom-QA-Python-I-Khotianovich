import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions


from data.Data import *
from mysql_orm.mysql_orm_client import MysqlOrmConnection
from mysql_orm.orm_builder import MysqlOrmBuilder
from ui.pages.AuthorizationPage import AuthorizationPage
from ui.pages.AuthorizedPage import AuthorizedPage
from ui.pages.RegistrationPage import RegistrationPage


class NotChrome(Exception):
    pass


@pytest.fixture(scope="function")
def driver(config):
    """
    Need for UI test with Chrome
    :param config: config of browser
    """
    browser = config["browser"]
    version = config['version']
    selenoid = config["selenoid"]
    url = ''

    if browser == "chrome":
        if selenoid != 'True':
            url = config["url"]
            manager = ChromeDriverManager(version=version)
            driver = webdriver.Chrome(executable_path=manager.install())
        else:
            selenoid = 'http://0.0.0.0:4444/wd/hub'
            url = config['url_sel']
            options = ChromeOptions()
            options.add_argument("--window-size=800,600")

            prefs = {"download.default_directory": '/tmp'}
            options.add_experimental_option('prefs', prefs)
            capabilities = {'acceptInsecureCerts': True,
                            'browserName': browser,
                            'version': version,
                            }
            driver = webdriver.Remote(command_executor=selenoid,
                                      options=options,
                                      desired_capabilities=capabilities)
    else:
        raise NotChrome("Sorry, work only with chrome")

    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def authorization_page(driver):
    """
    Make an authorization page
    :param driver: webdriver
    :return: authorization page
    """
    return AuthorizationPage(driver)


@pytest.fixture(scope="function")
def authorized_page(driver, add_del_valid_user):
    """
    Make authorized page
    :param add_del_valid_user:
    :param driver: webdriver
    :return: AuthorizedPage as user with
    nick username = USER3, password = PASSWORD3
    """
    page = AuthorizationPage(driver)
    page.authorize(add_del_valid_user['u'], add_del_valid_user['p'])
    yield AuthorizedPage(page.driver)



@pytest.fixture(scope="function")
def registration_page(driver):
    """
    Make registration page
    :param driver: webdriver
    :return: RegistrationPage
    """
    page = AuthorizationPage(driver)
    page.go_registration()
    return RegistrationPage(page.driver)
