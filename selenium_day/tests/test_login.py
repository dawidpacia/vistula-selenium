from selenium_day.pages import LoginPage
from selenium_day.pages import MainPage


def test_login(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    main_page.go_to_login()
    login_page.login()
