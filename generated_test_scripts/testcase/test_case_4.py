
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = driver.find_element(By.XPATH, '//*[@id="user-name"]')
        self.password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
        self.login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')

    def login(self, username, password):
        self.username_field.send_keys(username)
        self.password_field.send_keys(password)
        time.sleep(3)  # Wait for 3 secs
        self.login_button.click()

class UITestScenario:
    def __init__(self, driver):
        self.driver = driver

    def add_items_to_cart(self):
        bike_light = self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        fleece_jacket = self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        bike_light.click()
        time.sleep(3)  # Wait for 3 secs
        fleece_jacket.click()

    def proceed_to_checkout(self):
        cart_icon = self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        cart_icon.click()
        time.sleep(3)  # Wait for 3 secs
        checkout = self.driver.find_element(By.XPATH, '//*[@id="checkout"]')
        checkout.click()

    def enter_checkout_details_and_continue(self):
        first_name_field = self.driver.find_element(By.XPATH, '//*[@id="first-name"]')
        last_name_field = self.driver.find_element(By.XPATH, '//*[@id="last-name"]')
        zip_code_field = self.driver.find_element(By.XPATH, '//*[@id="postal-code"]')
        continue_button = self.driver.find_element(By.XPATH, '//*[@id="continue"]')

        first_name_field.send_keys('somename')
        last_name_field.send_keys('lastname')
        zip_code_field.send_keys('123456')
        time.sleep(3)  # Wait for 3 secs
        continue_button.click()

    def verify_payment_information_label(self):
        payment_info_label = self.driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')
        assert payment_info_label.is_displayed()

def test_ui_scenario():
    driver = webdriver.Chrome()
    driver.get("https://www.example.com")  # replace with actual URL

    login_page = LoginPage(driver)
    login_page.login("username", "password")

    ui_test = UITestScenario(driver)

    ui_test.add_items_to_cart()
    ui_test.proceed_to_checkout()
    ui_test.enter_checkout_details_and_continue()
    ui_test.verify_payment_information_label()

    driver.quit()

if __name__ == "__main__":
    test_ui_scenario()
