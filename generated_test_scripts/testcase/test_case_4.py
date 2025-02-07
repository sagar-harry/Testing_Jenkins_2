
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        user_field = self.driver.find_element(By.XPATH, '//*[@id="user-name"]')
        pass_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')

        user_field.send_keys(username)
        time.sleep(3)
        pass_field.send_keys(password)
        time.sleep(3)

        login_button.click()
        time.sleep(5)

def run_test():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--incognito')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get('URL_OF_THE_APPLICATION')
        time.sleep(5)
        driver.maximize_window()
        time.sleep(3)

        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')

        bike_light = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        cart_icon = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        checkout = driver.find_element(By.XPATH, '//*[@id="checkout"]')
        first_name = driver.find_element(By.XPATH, '//*[@id="first-name"]')
        last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        zip_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
        continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
        payment_info_card = By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'

        bike_light.click()
        time.sleep(3)
        fleece_jacket.click()
        time.sleep(3)
        cart_icon.click()
        time.sleep(3)
        checkout.click()
        time.sleep(3)

        first_name.send_keys('somename')
        time.sleep(3)
        last_name.send_keys('lastname')
        time.sleep(3)
        zip_code.send_keys('123456')
        time.sleep(3)

        continue_button.click()
        time.sleep(5)

        if driver.find_element(*payment_info_card).is_displayed():
            exit_code = 0
        else:
            exit_code = 1

    except Exception as e:
        print(f"Test failed: {e}")
        exit_code = 1

    driver.quit()
    exit(exit_code)

if __name__ == "__main__":
    run_test()
