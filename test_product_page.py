from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import pytest
import pytest
import time

#product_url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
product_url = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_items_in_basket()
    page.should_be_basket_is_empty()

@pytest.mark.skip()
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_url, 4)
    page.open()
    page.add_product_to_basket()
    page.should_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, product_url)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_url)
    page.open()
    page.go_to_login_page()


@pytest.mark.login
class TestLoginFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = ProductPage(browser, product_url, 4)
        page.open()
        yield page
        print("\nfinish")

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, setup):
        setup.add_product_to_basket()
        setup.should_not_be_success_message()

    def test_check_current_language(self, browser):
        language = browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        print(language)


@pytest.mark.registration
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        page = LoginPage(browser, product_url, 4)
        page.open()
        page.register_new_user(email, "kjghskjhgslkhgls")
        page.should_be_authorized_user()
        yield page
        print("\nfinish test")

    def test_user_cant_see_success_message(self, setup):
        setup.should_not_be_success_message()

    """@pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              pytest.param(
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  marks=pytest.mark.skip),
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])"""
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, product_url, 4)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
