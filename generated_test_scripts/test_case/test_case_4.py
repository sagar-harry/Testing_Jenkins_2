
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username: str, password: str):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

def test_payment_info_displayed():
    driver = webdriver.Chrome()
    driver.get("http://example.com")  # Replace with the actual URL

    # Login Process
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")  # Replace with actual credentials

    # Add products to cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()

    # Proceed to checkout
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    cart_badge.click()

    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    # Enter checkout information
    driver.find_element(By.ID, "first-name").send_keys("somename")
    driver.find_element(By.ID, "last-name").send_keys("lastname")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

    # Verify payment information label
    payment_info_label = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='payment-info-label']")))
    assert payment_info_label is not None

    print("Test Passed: Payment Information label is visible.")
    driver.quit()

if __name__ == "__main__":
    test_payment_info_displayed()
