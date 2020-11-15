from selenium_day.webdriver.common.by import By
from selenium_day.pages import BasePage


class MainPage(BasePage):

    login_selector = (By.CLASS_NAME, "login")

    def go_to_login(self):
        self.driver.find_element(*self.login_selector).click()