
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

class UITest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.example.com")  # Replace with the actual URL
        self.login_page = LoginPage(self.driver)

    def test_checkout_payment_information(self):
        self.login_page.login("standard_user", "secret_sauce")
        
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("somename")
        self.driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
        self.driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")
        
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        
        time.sleep(3)
        payment_info_visible = self.driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]').is_displayed()
        self.assertTrue(payment_info_visible, "Payment Information label is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
