from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    LOGIN_PAGE = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_INPUT = (By.CSS_SELECTOR, "#id_login-username[type='email']")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")