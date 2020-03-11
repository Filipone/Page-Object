from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import pytest

url = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=midsummer"


@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser):
        page = LoginPage(browser, url, 3)
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
        page.should_be_login_link()
        page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = BasketPage(browser, url, 3)
        page.open()
        page.go_to_basket_page()
        page.should_not_be_items_in_basket()
        page.should_be_basket_is_empty()
