from pages.home_page import HomePage


class TestCalculator:

    # def setup_method(self, driver):
    #     self.home_page = HomePage(driver)

    def test_add(self, driver):
        self.home_page = HomePage(driver)
        self.home_page.add_numbers()
        result = self.home_page.get_result()
        assert result == "3"

    def test_sub(self, driver):
        self.home_page = HomePage(driver)
        self.home_page.sub_numbers()
        result = self.home_page.get_result()
        assert result == "−1"
#
# def test_mul():
#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable(digit_1_selector)).click()
#     driver.find_element(*multiply_selector).click()
#     driver.find_element(*digit_2_selector).click()
#     driver.find_element(*equals_selector).click()
#     result_value = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(result_selector)).text
#     assert result_value == "2"
#
# def test_div():
#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable(digit_1_selector)).click()
#     driver.find_element(*divide_selector).click()
#     driver.find_element(*digit_2_selector).click()
#     driver.find_element(*equals_selector).click()
#     result_value = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(result_selector)).text
#     assert result_value == "0.5"