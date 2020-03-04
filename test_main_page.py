from pages.main_page import MainPage
from pages.login_page import LoginPage

url = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=midsummer"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, url,
                    3)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
    page.should_be_login_link()


def test_second_guest_can_go_to_login_page(browser):
    page2 = LoginPage(browser, url, 3)
    page2.should_be_login_page()
