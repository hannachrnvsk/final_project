import math
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from final_project.pages.locators import BasePageLocators



class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def is_element_present(self,method, locator):
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((method,locator)))
        except NoSuchElementException:
            return False
        return True

    def return_element_located(self,method,locator):
        elt = self.browser.find_element(method,locator)
        return elt

    def get_current_url(self):
        cur_url = self.browser.current_url
        return cur_url

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def click_button(self, method, locator):
        self.browser.find_element(method, locator).click()

    def get_text_of_element(self,method, locator):
        self.browser.find_element(method,locator).text()

    def is_disappeared(self, method, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((method, locator)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, method, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((method, locator)))
        except TimeoutException:
            return True
        return False



