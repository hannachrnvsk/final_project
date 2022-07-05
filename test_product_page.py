from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
import pytest


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

"""@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])"""
def test_guest_can_add_product_to_basket(browser):
    """Один из тестов должен находить баг.
     Но пока не находит. Надо разобраться почему и починить."""
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    add_to_basket = page.presence_of_elt_located(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
    add_to_basket.click()
    # page.solve_quiz_and_get_code()
    assert page.return_element_lacated(*ProductPageLocators.ADD_TO_BASKET_BUTTON).text == "Ajouter au panier"

