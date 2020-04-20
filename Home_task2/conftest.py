import pytest
from ui.fixtures_UI import *


def pytest_addoption(parser):
    parser.addoption('--url', default='https://target.my.com')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_v', default='latest')
    parser.addoption('--selenoid', default=False)


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_v')
    selenoid = request.config.getoption('--selenoid')

    return {'browser': browser, 'version': version, 'url': url,
            'selenoid': selenoid}
