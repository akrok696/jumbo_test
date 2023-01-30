from selenium.webdriver.common.by import By
from tools import consts


def test_2_user_login(driver):
    """ This is a test case to test the Jumbo Login Page.

        ACTION:
            1. Load Jumbo.com web page
            2. Close cookies consent
            3. Open user menu
            4. Check shopping list
            5. Check "Inloggen" button
    """
    driver.get(consts.HOME_PAGE)
    driver.implicitly_wait(10)
    driver.find_element(By.ID, consts.REJECT_COOKIES).click()
    driver.find_element(By.XPATH, "//button[contains(@id, 'jum_user_menu_large_button')]").click()
    driver.find_element(By.XPATH, "//a[contains(@class, 'item-link') and text() = ' Inloggen ']")

    """ Test was divided into two tests due to security problems, web driver is not able to open links"""
