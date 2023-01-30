import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from tests import *


class Tests(unittest.TestCase):
    """ This is a test suit for tests. Which includes test setup and teardown

            Setup actions:
                1. Install Chromium webdriver and start it with options
                2. Maximize webdriver window
            Teardown actions:
                3. Delete all cookies
                4. Quit from webdriver
    """

    def setUp(self):
        self.options = Options()
        self.options.add_argument("start-maximized")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(options=self.options, service=Service(ChromeDriverManager().install()))
        self.driver.delete_all_cookies()
        self.driver.maximize_window()

    def test_1_welcome_page(self):
        test_1_welcome_page.test_1_welcome_page(self.driver)

    def test_2_user_login(self):
        test_2_user_login.test_2_user_login(self.driver)

    def test_2_1_user_login(self):
        test_2_1_user_login.test_2_1_user_login(self.driver)

    def test_3_product_search(self):
        test_3_product_search.test_3_product_search(self.driver)

    def test_4_product_details(self):
        test_4_product_details.test_4_product_details(self.driver)

    def test_5_add_product(self):
        test_5_add_product.test_5_add_product(self.driver)

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
