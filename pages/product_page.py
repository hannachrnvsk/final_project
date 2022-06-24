from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_description()
        self.should_be_product_info()
        self.should_be_button_addtochart()

    def should_be_product_description(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_DESCRIPTION_FIELD), "Product description is not presented"

    def should_be_product_info(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_INFO_FIELD), "Product info field is not presented"

    def should_be_button_addtochart(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON),"Button 'Add to basket' is not presented"


