from selenium.webdriver.common.by import By


class AuthorizationLocators:
    FULL_PENETRATION_BUTTON = (
        By.CLASS_NAME, "responseHead-module-button-1BMAy4")

    EMAIL_FIELD = (By.NAME, "email")

    PASSWORD_FIELD = (By.NAME, "password")

    CHECK_AUTH_SUCCESS = (By.CLASS_NAME, "right-module-userNameWrap-34ibLS")
