from .product_page import ProductPage
from .locators import LoginPageLocators


class LoginPage(ProductPage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Url don't have login"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_INPUT), "Problem with login-input"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Problem with register-form"

    def register_new_user(self, email, password):
        self.go_to_login_page()
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT).click()
