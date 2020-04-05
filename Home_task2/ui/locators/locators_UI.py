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


class CreateSegmentLocators:
    AUDITORIUMS = (By.XPATH,
                   '//a[contains(@href, "/segments")]')
    CREATE_SEGMENT_BUTTON = (By.PARTIAL_LINK_TEXT, 'Создайте')
    CREATE_SEGMENT_BUTTON_NOT_FIRST = (
        By.XPATH, '// div[contains(text(), "Создать сегмент")]')
    NAME_EDIT = (By.XPATH, '// div[contains(@class , "input__wrap")]/' +
                 'input[contains(@maxlength, "60")]')
    ADD_AUDITORIUM_SEGMENT = (By.XPATH, '//span[contains(@data-loc-ru,' +
                              '"Добавить аудиторные сегменты...")]')
    APPS_CHOICE = (By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div/div[2]' +
                   '/div/div[2]/div[1]/div[9]')
    PLAYED_CHOICE = (By.CLASS_NAME, 'js-source-name')
    PAYED_CHOICE = (By.XPATH,
                    '//span[contains(@data-loc-ru,"Платившие в платформе")]')
    ADD_SEGMENT = (By.XPATH,
                   '//div[contains(text(), "Добавить сегмент")]')
    CREATE_SEGMENT = (By.XPATH, '//div[contains(text(), "Создать сегмент")]')


class DeleteSegmentLocators:
    AUDITORIUMS = (By.XPATH,
                   '//a[contains(@href, "/segments")]')
    SEARCH_EDIT = (By.CLASS_NAME, 'suggester-ts__input')
    CROSS = (By.XPATH,
             '//div[contains(@class, "remove-source-wrap js-remove-source")]')
    DELETE_BUTTON = (By.XPATH, '//div[contains(text(), "Удалить")]')
