from pages.main_page import MainPage
from pages.login_page import LoginPage

url = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=midsummer"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, url, 3)
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
    page.should_be_login_link()
    login_page = LoginPage(browser, url)
    login_page.should_be_login_page()
