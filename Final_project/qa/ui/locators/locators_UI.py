from selenium.webdriver.common.by import By


class AuthorizationLocators:
    USERNAME_FIELD = (By.ID, 'username')
    PASSWORD_FIELD = (By.ID, 'password')
    FULL_PENETRATION_BUTTON = (By.ID, 'submit')

    CHECK_AUTH_SUCCESS = (By.ID, 'logout')
    CHECK_AUTH_FAILED = USERNAME_FIELD

    REGISTRATION = (By.PARTIAL_LINK_TEXT, 'Create an account')
    REGISTRATION_SUBMIT = (By.ID, 'submit')

    LOGOUT_BUTTON = (By.ID, 'logout')


class LogOutLocators:
    LOGOUT_BUTTON = (By.ID, 'logout')
    FULL_PENETRATION_BUTTON = (By.ID, 'submit')


class RegLocators:
    USERNAME_FIELD = (By.ID, 'username')
    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.ID, 'password')
    PASSWORD_CONF_FIELD = (By.ID, 'confirm')
    TERM = (By.ID, 'term')
    REG_BUTTON = (By.ID, 'submit')
    LOGOUT_BUTTON = LogOutLocators.LOGOUT_BUTTON
    REGISTRATION = (By.PARTIAL_LINK_TEXT, 'Create an account')
    VK_ID = (By.XPATH, '//*[@id="login-name"]/ul/li[2]')


class AuthorizedPageLocators:
    LOGOUT_BUTTON = (By.ID, 'logout')
    FULL_PENETRATION_BUTTON = (By.ID, 'submit')

    HOME_BUTTON = (By.XPATH, '//*[@id="wrap"]/header/nav/ul/li[1]/a')

    FACT = (By.XPATH, '/html/body/footer/div/p[2]')

    PICTURE_ONE_BUTTON = (
        By.XPATH, '//*[@id="content"]/div[2]/div[1]/figure/a/img')
    PICTURE_THREE_BUTTON = (
        By.XPATH, '//*[@id="content"]/div[2]/div[3]/figure/a/img')
    PICTURE_TWO_BUTTON = (
        By.XPATH, '//*[@id="content"]/div[2]/div[2]/figure/a/img')

    PYTHON_BUTTON = (By.XPATH, '//*[@id="wrap"]/header/nav/ul/li[2]')
    PYTHON_HISTORY = (
        By.XPATH, '//*[@id="wrap"]/header/nav/ul/li[2]/div/ul/li[1]/a')
    FLASK_BUTTON = (
        By.XPATH, '//*[@id="wrap"]/header/nav/ul/li[2]/div/ul/li[2]/a')

    LINUX_BUTTON = (By.XPATH, '//*[@id="wrap"]/header/nav/ul/li[3]/a')
    DOWNLOAD_CENT_OS = \
        (By.XPATH, '//*[@id="wrap"]/header/nav/ul/li[3]/div/ul/li/a')

    NETWORK_BUTTON = (By.XPATH, '//*[@id="wrap"]/header/nav/ul/li[4]/a')
    NETWORK_NEWS = (
        By.XPATH,
        '//*[@id="wrap"]/header/nav/ul/li[4]/div/ul/li[1]/ul/li[1]/a')
    NETWORK_DOWNLOAD = (
        By.XPATH,
        '//*[@id="wrap"]/header/nav/ul/li[4]/div/ul/li[1]/ul/li[2]/a')
    NETWORK_EXAMPLE = (
        By.XPATH,
        '//*[@id="wrap"]/header/nav/ul/li[4]/div/ul/li[2]/ul/li/a')
