from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage


def test_shop1(browser):
    # пробный
    # не имеет отношения ко всему остальному
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    review = browser.find_element(By.CSS_SELECTOR, "a#write_review")
    review.click()
    new = browser.current_url
    btn_text = browser.find_element(By.CSS_SELECTOR, "fieldset>button[type=submit]").text
    assert btn_text == "Save review", f'new page is  {new}, first page was {link}'


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()




