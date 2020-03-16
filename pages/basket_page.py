from pages.base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException


class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        try:
            self.browser.find_element(*BasketPageLocators.BASKET_ITEMS)
            assert False
        except NoSuchElementException:
            assert True

    def should_be_basket_is_empty(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Сообщения показывает что корзина не пуста"