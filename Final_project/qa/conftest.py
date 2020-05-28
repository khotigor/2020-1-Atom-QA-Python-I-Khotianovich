import time
from urllib.parse import urljoin

import decorator
import requests
import allure

from ui.fixtures_UI import *

import os


def pytest_addoption(parser):
    parser.addoption('--url_sel', default='http:/myapp:3320')  # selenoid
    parser.addoption('--url', default='http:/0.0.0.0:3320')  # no selenoid
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_v', default='latest')
    parser.addoption('--selenoid', default=False)


@pytest.fixture(scope='session')
def config(request):
    url_sel = request.config.getoption('--url_sel')
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_v')
    selenoid = request.config.getoption('--selenoid')

    return {'browser': browser, 'version': version, 'url': url,
            'selenoid': selenoid, 'url_sel': url_sel}


class DBConf:
    db_login = 'test_qa'
    db_password = 'qa_test'
    db_name = 'technoatom'
    db_loc_host = '0.0.0.0'
    db_host = '0.0.0.0'
    db_port = '3306'


@pytest.fixture(scope='session')
def mysql_orm_client():
    return MysqlOrmConnection(
        user=DBConf.db_login,
        password=DBConf.db_password,
        db_name=DBConf.db_name,
        local_host=DBConf.db_loc_host,
        host=DBConf.db_host,
        port=DBConf.db_port
    )


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function", autouse=True)
def take_screenshot_when_failure(request, driver):
    yield
    if request.node.rep_call.failed:
        allure.attach(
            '\n'.join([a['message'] for a in driver.get_log('browser')]),
            name='console.log',
            attachment_type=allure.attachment_type.TEXT)
        allure.attach(driver.get_screenshot_as_png(),
                      name=request.node.location[-1],
                      attachment_type=allure.attachment_type.PNG)


def pytest_report_header():
    """just a header"""
    return "\n\n These tests were made by Igor Khotianovich \n " \
           "NRNU MEPhI, 2020"" \n\n"


def pytest_sessionstart():
    """ called before ``pytest_runtest_call(item). """
    os.system('docker-compose up -d')


def pytest_sessionfinish():
    """ called after ``pytest_runtest_call(item). """
    os.system('sleep 30 && docker-compose down')


@pytest.fixture(scope='session')
def wait_for_docker():
    time.sleep(10)
    base_url = 'http://0.0.0.0:3320/'
    session = requests.Session()
    location = 'status'
    url = urljoin(base_url, location)
    i = 0
    while i < 5:
        i = i + 1
        time.sleep(5)
        request = session.request('GET', url)
        if request.status_code == 200:
            break
