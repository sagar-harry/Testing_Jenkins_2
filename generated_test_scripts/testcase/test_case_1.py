
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = '//*[@id="user-name"]'
        self.password_locator = '//*[@id="password"]'
        self.login_button_locator = '//*[@id="login-button"]'

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.username_locator)))
        self.driver.find_element(By.XPATH, self.username_locator).send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.password_locator).send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.login_button_locator).click()
        time.sleep(3)

def test_complete_purchase_flow():
    try:
        driver = webdriver.Chrome()
        driver.get('https://example.com/login')
        driver.maximize_window()
        time.sleep(5)

        # Login
        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')

        # Add items to cart
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
        time.sleep(3)

        # Go to cart
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)

        # Proceed to checkout
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        time.sleep(3)

        # Enter checkout information
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))).send_keys('somename')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('lastname')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('123456')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        time.sleep(3)

        # Complete the purchase
        driver.find_element(By.XPATH, '//*[@id="finish"]').click()
        time.sleep(3)

        # Return to homepage
        driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
        time.sleep(3)

        # Logout
        driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
        time.sleep(3)

        driver.quit()
        return 0
    except Exception as e:
        print(f"Test failed: {e}")
        driver.quit()
        return 1

# Execute test
if __name__ == '__main__':
    result = test_complete_purchase_flow()
    exit(result)
