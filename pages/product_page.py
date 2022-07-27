from .base_page import BasePage
from .locators import ProductPageLocators, BasketPageLocators


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

    def click_addtochart_button(self):
        self.click_button(*ProductPageLocators.ADD_TO_BASKET_BUTTON)

    def go_to_basket(self):
        self.click_button(*ProductPageLocators.VIEW_BASKET_BUTTON)

    def should_be_message_empty_basket(self):
        assert 'empty' in self.return_element_located(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def  should_not_be_success_message_dis(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is presented, but should not be"