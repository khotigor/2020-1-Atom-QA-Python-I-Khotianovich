from selenium.webdriver.common.by import By


class AuthorizationLocators:
    EMAIL_FIELD = (By.NAME, 'email')
    PASSWORD_FIELD = (By.NAME, 'password')

    FULL_PENETRATION_BUTTON = (
        By.CLASS_NAME, 'responseHead-module-button-1BMAy4')

    CHECK_AUTH_SUCCESS = (By.CLASS_NAME, 'rightMenu-module-rightMenu-2GKiG5')
    CHECK_AUTH_FAILED = (By.CLASS_NAME, 'formMsg_text')


class CreateAdvertisingCampaignLocators:
    CREATE_ADVERTISING_CAMPAIGN = (By.PARTIAL_LINK_TEXT, 'создайте')
    CREATE_ADVERTISING_CAMPAIGN_NOT_FIRST = (
        By.XPATH, '//span[contains(@data-loc-ru, "Создать кампанию")]')
    TRAFFIC_TYPE_CAMPAIGN = (By.XPATH, '//div[contains(text(), "Трафик")]')
    LINK_EDIT = (By.XPATH, '//div[contains(@class, "input__wrap")]/' +
                 'input[contains(@placeholder, "Введите ссылку")]')
    NAME_EDIT = (By.XPATH, '//div[2]/input[contains(@class, ' +
                 '"input__inp js-form-element")]')
    DOWNLOAD = (By.XPATH, '//input[contains(@class, ' +
                '"input__inp input__inp_file js-form-element")]')
    BANNER = (By.ID, '192')
    BUTTON_CREATE = (By.XPATH, '//div[contains(text(), "Создать кампанию")]')
    CHECK = (By.XPATH,
             '//a[contains(@class, "campaigns-tbl-cell__campaign-name")]')
