import time
import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage

PRODUCT_URL = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_items_in_basket()
    page.should_be_basket_is_empty()


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                               marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()


@pytest.mark.skip()
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_URL, 4)
    page.open()
    page.add_product_to_basket()
    page.should_disappeared_success_message()


@pytest.mark.login
class TestLoginFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        product_url_without_alert = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, product_url_without_alert, 4)
        page.open()
        yield page
        print("\nfinish test")

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, setup):
        setup.add_product_to_basket()
        setup.should_not_be_success_message()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, PRODUCT_URL)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, PRODUCT_URL)
        page.open()
        page.should_be_login_link()

    def test_check_current_language(self, browser):
        language = browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        print(language)


@pytest.mark.registration
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="module")
    def setup(self, browser):
        page = LoginPage(browser, PRODUCT_URL, 4)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, "kjghskjhgslkhgls")
        page.should_be_authorized_user()
        yield page
        print("\nfinish test")

    def test_user_cant_see_success_message(self, setup):
        setup.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, setup):
        setup.open()
        setup.add_product_to_basket()
        setup.solve_quiz_and_get_code()
