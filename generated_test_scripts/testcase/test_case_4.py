
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = driver.find_element(By.XPATH, '//*[@id="user-name"]')
        self.password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
        self.login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')

    def login(self, username, password):
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_button.click()

class CheckoutTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Make sure to have the appropriate WebDriver installed
        self.driver.get("URL_OF_THE_APPLICATION")  # Substitute with the actual URL of the application

    def test_checkout_process(self):
        driver = self.driver
        # Login
        login_page = LoginPage(driver)
        login_page.login('your_username', 'your_password')  # Use actual credentials
        
        # Add items to cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        
        # Proceed to checkout
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        
        # Enter checkout details
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('somename')
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('lastname')
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('123456')
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        
        # Verify Payment Information is displayed
        payment_info = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')
        self.assertTrue(payment_info.is_displayed(), "Payment Information label is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
