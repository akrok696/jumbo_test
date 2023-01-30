from selenium.webdriver.common.by import By
from tools import consts


def test_3_product_search(driver):
    """ This is a test case to test the Jumbo Product Search.

        ACTION:
            1. Load Jumbo web page with search results
            2. Close cookies consent
            3. Check Results for Unicorn
            4. Check price for all products
            5. Check categories count
    """
    driver.get(consts.SEARCH_RESULTS_PAGE)
    driver.implicitly_wait(10)
    driver.find_element(By.ID, consts.REJECT_COOKIES).click()
    res = driver.find_elements(By.XPATH, consts.SEARCH_RESULTS)
    for i in res:
        assert "Unicorn" in i.text, '"Unicorn" is missed in data'
    driver.find_elements(By.XPATH, consts.PRICE_FOR_ALL_PRODUCTS)
    cat = driver.find_elements(By.XPATH, consts.CATEGORIES_COUNT)
    for i in cat:
        try:
            assert int(i.text[1:-1]) > 0, "Wrong Categories count!"
        except ValueError:
            raise AssertionError("Categories count has invalid data")
