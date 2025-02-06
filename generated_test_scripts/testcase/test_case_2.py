
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

# Assuming LoginPage class is defined elsewhere in the project
from LoginPage import LoginPage

class TestUICartFunctionality(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://your-application-url.com")  # Add the URL of the web application
        self.driver.maximize_window()
        time.sleep(2)

    def test_add_items_to_cart_and_verify_count(self):
        driver = self.driver

        # Login using LoginPage class method
        login_page = LoginPage(driver)
        login_page.login()

        # Add 'Bike Light' to cart
        bike_light = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        bike_light.click()

        # Add 'Fleece Jacket' to cart
        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        fleece_jacket.click()

        time.sleep(2)  # Wait to ensure items are added

        # Verify cart badge displays '2'
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        self.assertEqual(cart_count.text, '2', "Cart count is not correct. Expected: 2, Found: " + cart_count.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
