
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = '//*[@id="user-name"]'
        self.password_input = '//*[@id="password"]'
        self.login_button = '//*[@id="login-button"]'

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.username_input))
        )
        self.driver.find_element(By.XPATH, self.username_input).send_keys(username)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.password_input))
        )
        self.driver.find_element(By.XPATH, self.password_input).send_keys(password)

        time.sleep(3)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.login_button))
        )
        self.driver.find_element(By.XPATH, self.login_button).click()

def test_add_to_cart():
    try:
        driver = webdriver.Chrome()
        driver.get("https://www.example.com")

        login_page = LoginPage(driver)
        login_page.login("testuser", "testpassword")

        time.sleep(3)
        
        bike_light_xpath = '//*[@id="add-to-cart-sauce-labs-bike-light"]'
        fleece_jacket_xpath = '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
        cart_count_xpath = '//*[@id="shopping_cart_container"]/a/span'
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, bike_light_xpath))
        )
        driver.find_element(By.XPATH, bike_light_xpath).click()

        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, fleece_jacket_xpath))
        )
        driver.find_element(By.XPATH, fleece_jacket_xpath).click()

        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, cart_count_xpath))
        )
        cart_count = driver.find_element(By.XPATH, cart_count_xpath).text

        time.sleep(3)

        driver.quit()

        if cart_count == "2":
            print("Test Passed")
            return 0
        else:
            print("Test Failed")
            return -1

    except Exception as e:
        print("An exception occurred:", str(e))
        driver.quit()
        return -1

if __name__ == "__main__":
    result = test_add_to_cart()
    exit(result)
