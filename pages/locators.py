from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group>a")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group>a")


class LoginPageLocators:
    REG_FORM = (By.CSS_SELECTOR, "form#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group>a")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "form#add_to_basket_form>button[type=submit]")
    PRODUCT_INFO_FIELD = (By.CSS_SELECTOR, "div.sub-header+table" )
    PRODUCT_DESCRIPTION_FIELD =(By.CSS_SELECTOR,"div#product_description" )
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR , "span.btn-group>a")
    TOTAL_IN_BASKET = (By.CSS_SELECTOR, "div.basket-mini")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, "h1+p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success')


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "div#content_inner>p")

