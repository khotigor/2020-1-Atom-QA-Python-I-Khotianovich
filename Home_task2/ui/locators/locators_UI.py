from selenium.webdriver.common.by import By


class AuthorizationLocators:
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")

    FULL_PENETRATION_BUTTON = (
        By.CLASS_NAME, "responseHead-module-button-1BMAy4")

    CHECK_AUTH_SUCCESS = (By.CLASS_NAME, "rightMenu-module-rightMenu-2GKiG5")
    CHECK_AUTH_FAILED = (By.CLASS_NAME, "formMsg_text")
