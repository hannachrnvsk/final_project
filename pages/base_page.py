import math
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.support import expected_conditions as  EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def presence_of_elt_located(self, method,locator):
        element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((method,locator)))
        return element

    def is_element_present(self,method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True

    def return_element_lacated(self,method,locator):
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
