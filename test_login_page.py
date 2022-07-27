import pytest
from selenium.webdriver.common.by import By
from final_project.pages.locators import LoginPageLocators
from pages.login_page import LoginPage


link = "https://selenium1py.pythonanywhere.com/accounts/login/"


def test_login_page_exists(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()



