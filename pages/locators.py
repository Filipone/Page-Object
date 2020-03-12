from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    LOGIN_PAGE = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_INPUT = (By.CSS_SELECTOR, "#id_login-username[type='email']")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#nav.navbar-right.navbar-nav")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "a.registration_link")


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "div#content_inner")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "ul.nav.navbar-nav.navbar-right")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#invalid_locator")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, "div.alert.alert-success.fade.in")
