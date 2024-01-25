from selenium.webdriver.common.by import By
from tools import consts


def test_2_1_user_login(driver):
    """ This is a test case to test the Jumbo Login Page.

        ACTION:
            1. Load Jumbo login web page
            2. Close cookies consent
            3. Enter valid user email
            4. Enter valid user password
            5. Click on login button
    """
    driver.get(consts.LOGIN_PAGE)
    driver.implicitly_wait(10)
    driver.find_element(By.ID, consts.REJECT_COOKIES).click()
    driver.find_element(By.NAME, consts.USERNAME_INPUT).send_keys('akrok696@gmail.com')  # Username
    driver.find_element(By.NAME, consts.PASSWORD_INPUT).send_keys('123test456')  # Password
    driver.find_element(By.XPATH, consts.LOGIN_BUTTON).click()
    """ Test was divided into two tests due to security problems, 
    web driver is not able to get response from the server"""
