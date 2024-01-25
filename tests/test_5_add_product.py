from selenium.webdriver.common.by import By
from tools import consts


def test_5_add_product(driver):
    """ This is a test case to test the Jumbo Product Details.

        ACTION:
            1. Load Jumbo web page with details for product
            2. Close cookies consent
            3. Add product to basket
            4. Check basket count
            5. Remove product from basket
            6. Check basket count
    """
    driver.get(consts.DETAILED_PRODUCT_PAGE)
    driver.implicitly_wait(10)
    driver.find_element(By.ID, consts.REJECT_COOKIES).click()
    empty_basket= driver.find_elements(By.CSS_SELECTOR, consts.BASKET_COUNT)
    basket_count = [element.text for element in empty_basket]
    assert not basket_count

    driver.find_element(By.CSS_SELECTOR, consts.ADD_TO_BASKET_MAIN).click()
    count_add = driver.find_elements(By.CSS_SELECTOR, consts.BASKET_COUNT)
    basket_count = [element.text for element in count_add]
    assert int(basket_count[0]) == 1, "Count wrong!"

    driver.find_element(By.CSS_SELECTOR, consts.REMOVE_FROM_BASKET).click()
    count_remove = driver.find_elements(By.CSS_SELECTOR, consts.BASKET_COUNT)
    basket_count = [element.text for element in count_remove]
    assert not basket_count
    """Test fails due to fast clicking on REMOVE_FROM_BASKET button"""
