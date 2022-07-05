from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REG_FORM = (By.CSS_SELECTOR, "form#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "form#add_to_basket_form>button[type=submit]")
    PRODUCT_INFO_FIELD = (By.CSS_SELECTOR, "div.sub-header+table" )
    PRODUCT_DESCRIPTION_FIELD =(By.CSS_SELECTOR,"div#product_description" )

