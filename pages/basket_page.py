from .base_page import BasePage
from .locators import BasketPageLocators
import pytest

class BasketPage(BasePage):
    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), \
            "some product is"

    def basket_should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Basket isnt empty"
