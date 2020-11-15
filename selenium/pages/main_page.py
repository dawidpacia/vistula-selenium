from selenium.webdriver.common.by import By
from selenium.pages import BasePage


class MainPage(BasePage):

    login_selector = (By.CLASS_NAME, "login")

    def go_to_login(self):
        self.driver.find_element(*self.login_selector).click()