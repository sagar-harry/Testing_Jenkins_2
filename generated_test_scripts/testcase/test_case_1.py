
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestPurchaseFlow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.yourwebsite.com")  # Replace with the actual URL

    def test_purchase_flow(self):
        driver = self.driver
        
        # login
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')  # Replace with valid username
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')    # Replace with valid password
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

        # add items to cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        
        # go to cart
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        
        # proceed to checkout
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()

        # enter checkout information
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('somename')
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('lastname')
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('123456')
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()

        # complete purchase
        driver.find_element(By.XPATH, '//*[@id="finish"]').click()
        
        # Back to homepage
        driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()

        # logout
        driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
        time.sleep(2)  # Allow animation to finish
        driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()

        # Verify successful logout
        self.assertTrue(driver.find_element(By.XPATH, '//*[@id="login-button"]').is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
