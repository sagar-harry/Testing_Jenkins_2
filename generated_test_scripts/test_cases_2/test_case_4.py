
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

class UITestScenario(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Use the appropriate WebDriver for your browser
        self.driver.get("http://example.com")  # Use the correct URL for the site you're testing

    def test_payment_information_visibility(self):
        driver = self.driver

        # Step 1: Log in
        login_page = LoginPage(driver)
        login_page.login("your_username", "your_password")

        # Step 2: Add 'Bike Light' to the cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

        # Step 3: Add 'Fleece Jacket' to the cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()

        # Step 4: Proceed to checkout
        driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()
        driver.find_element(By.ID, "checkout").click()

        # Step 5: Enter First Name, Last Name, and Zip Code
        driver.find_element(By.ID, "first-name").send_keys("somename")
        driver.find_element(By.ID, "last-name").send_keys("lastname")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        
        # Step 6: Click 'Continue'
        driver.find_element(By.ID, "continue").click()

        # Step 7: Verify 'Payment Information' label is visible
        payment_info_label = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='payment-info-label']"))
        )
        self.assertTrue(payment_info_label.is_displayed(), "Payment Information label is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
