
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

class UITest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def setup(self):
        self.driver.get("URL_OF_THE_APPLICATION")
        self.login_page = LoginPage(self.driver)
        self.login_page.login('standard_user', 'secret_sauce')
        time.sleep(3)

    def test_add_items_to_cart(self):
        self.setup()
        
        # Add 'Bike Light' to cart
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)

        # Add 'Fleece Jacket' to cart
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Verify cart badge displays '2'
        cart_count = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
        assert cart_count.text == '2'

    def test_reset_cart(self):
        self.setup()
        
        # Reset cart (assumption: button is available to reset cart)
        self.driver.find_element(By.XPATH, 'Xpath for reset button').click()
        time.sleep(3)

        # Verify cart is empty
        cart_count_elements = self.driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert len(cart_count_elements) == 0

    def test_add_after_reset(self):
        self.setup()

        # Perform a reset to ensure clean state
        self.driver.find_element(By.XPATH, 'Xpath for reset button').click()
        time.sleep(3)

        # Add 'Bolt T-Shirt' to cart
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Verify cart badge displays '1'
        cart_count = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
        assert cart_count.text == '1'

    def teardown(self):
        self.driver.quit()

if __name__ == '__main__':
    ui_test = UITest()
    ui_test.test_add_items_to_cart()
    ui_test.test_reset_cart()
    ui_test.test_add_after_reset()
    ui_test.teardown()
