from selenium.webdriver.common.by import By
from tools import consts


def test_1_welcome_page(driver):
    """ This is a test case to test the Jumbo welcome page.

        ACTION:
            1. Load Jumbo.com web page
            2. Close cookies consent
            3. Check navigation panel
            4. Check shopping list
            5. Check product basket icon
    """

    driver.get(consts.HOME_PAGE)
    driver.implicitly_wait(10)
    driver.find_element(By.ID, consts.REJECT_COOKIES).click()
    nav = driver.find_elements(By.XPATH, consts.NAVI_PANEL)
    navi_panel_text = [element.text for element in nav]
    for i in consts.NAVI_LIST:
        assert i in navi_panel_text, "Objects not found"
    driver.find_elements(By.XPATH, consts.SHOPPING_LIST)
    driver.find_element(By.XPATH, consts.PRODUCT_BASKET)
    """Sometimes this test fails due to missing of PRODUCT_BASKET element"""
