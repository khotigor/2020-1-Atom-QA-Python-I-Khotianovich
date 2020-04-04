from selenium.webdriver.common.by import By


class AuthorizationLocators:
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")

    FULL_PENETRATION_BUTTON = (
        By.CLASS_NAME, "responseHead-module-button-1BMAy4")

    CHECK_AUTH_SUCCESS = (By.CLASS_NAME, "rightMenu-module-rightMenu-2GKiG5")
    CHECK_AUTH_FAILED = (By.CLASS_NAME, "formMsg_text")


class CreateAdvertisingCampaignLocators:
    CREATE_ADVERTISING_CAMPAIGN = (By.XPATH,
                                   "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[3]/div/div[3]/span/a")
    TRAFFIC_TYPE_CAMPAIGN = (By.XPATH, '//div[contains(text(), "Трафик")]')
    LINK_EDIT = (By.XPATH,
                 "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[2]/div/div[2]/div[1]/div[1]/div/div/input")
    NAME_EDIT = (By.XPATH,
                 "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[2]/div/div[7]/div/div[2]/div/div[2]/input")
    DOWNLOAD = (By.XPATH,
                '//input[contains(@class, "input__inp input__inp_file js-form-element")]')
    BANNER = (By.ID, '192')
    BUTTON_CREATE = (By.XPATH, '//div[contains(text(), "Создать кампанию")]')

    CHECK = (By.XPATH,
             "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[3]/div/div[2]/div[3]/div/div/div[1]/table/tbody/tr/td/div/div/table/tbody/tr/td[1]/div/div/div/a")
