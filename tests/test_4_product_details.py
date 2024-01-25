from selenium.webdriver.common.by import By
from tools import consts


def test_4_product_details(driver):
    """ This is a test case to test the Jumbo Product Details.

        ACTION:
            1. Load Jumbo web page with details for product
            2. Close cookies consent
            3. Check price for all products
            4. Check price per products
            5. Check add to basket button
            6. Check product breadcrumbs
    """
    driver.get(consts.DETAILED_PRODUCT_PAGE)
    driver.implicitly_wait(10)
    driver.find_element(By.ID, consts.REJECT_COOKIES).click()
    driver.find_elements(By.XPATH, consts.PRICE_FOR_ALL_PRODUCTS)
    driver.find_element(By.XPATH, consts.PRICE_PER_PRODUCT)
    driver.find_element(By.CSS_SELECTOR, consts.ADD_TO_BASKET_MAIN)
    driver.find_element(By.XPATH, consts.PRODUCT_BREADCRUMBS)
