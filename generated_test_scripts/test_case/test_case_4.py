
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

class CheckoutTest:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)

    def test_checkout_process(self):
        self.login_page.login('standard_user', 'secret_sauce')

        # Add 'Bike Light' to the cart
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

        # Add 'Fleece Jacket' to the cart
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()

        # Proceed to checkout
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()
        self.driver.find_element(By.ID, "checkout").click()

        # Enter checkout details
        self.driver.find_element(By.ID, "first-name").send_keys('somename')
        self.driver.find_element(By.ID, "last-name").send_keys('lastname')
        self.driver.find_element(By.ID, "postal-code").send_keys('123456')
        self.driver.find_element(By.ID, "continue").click()

        # Verify that the 'Payment Information' label is visible
        payment_info_label = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='payment-info-label']"))
        )

        assert payment_info_label.is_displayed(), "Payment Information label is not visible"

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')
    
    try:
        checkout_test = CheckoutTest(driver)
        checkout_test.test_checkout_process()
        print("Test passed: Payment Information label is visible.")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
