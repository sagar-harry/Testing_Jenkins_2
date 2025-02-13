
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def run_test():
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-notifications')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--incognito')

        driver = webdriver.Chrome(options=options)
        driver.get("https://saucedemo.com/")
        driver.maximize_window()
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()

        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()

        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]'))).send_keys("somename")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")

        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()

        time.sleep(3)
        payment_info_visible = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')))
        
        if payment_info_visible:
            print("Test passed")
            driver.quit()
            exit(0)
        else:
            print("Test failed")
            driver.quit()
            exit(1)

    except Exception as e:
        print(f"Test failed due to exception: {str(e)}")
        driver.quit()
        exit(1)

if __name__ == '__main__':
    run_test()
