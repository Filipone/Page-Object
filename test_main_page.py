def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)


def test_add_to_cart(browser):
    page = ProductPage(url="http://selenium1py.pythonanywhere.com/", browser)  # инициализируем объект Page Object
    page.open()  # открываем страницу в браузере
    page.should_be_add_to_cart_button()  # проверяем что есть кнопка добавления в корзину
    page.add_product_to_cart()  # жмем кнопку добавить в корзину
    page.should_be_success_message()  # проверяем что есть сообщение с нужным текстом
