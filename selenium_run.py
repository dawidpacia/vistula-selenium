from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get("http://automationpractice.com/index.php")

driver.find_element_by_id("search_query_top")

driver.quit()

