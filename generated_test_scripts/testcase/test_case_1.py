
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.XPATH, '//*[@id="user-name"]')
        self.password_locator = (By.XPATH, '//*[@id="password"]')
        self.login_button_locator = (By.XPATH, '//*[@id="login-button"]')

    def login(self, username, password):
        self.driver.find_element(*self.username_locator).send_keys(username)
        self.driver.find_element(*self.password_locator).send_keys(password)
        time.sleep(3)
        self.driver.find_element(*self.login_button_locator).click()

def run_test():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-popup-blocking")

    service = Service("/path/to/chromedriver")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    try:
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        ).click() 
        time.sleep(3)
        
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)
        
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)
        
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]'))
        ).send_keys("somename")
        
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        time.sleep(3)
        
        driver.find_element(By.XPATH, '//*[@id="finish"]').click()
        time.sleep(3)
        
        driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
        time.sleep(3)
        
        driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
        time.sleep(3)
        
        print("Test Passed")
        exit(0)

    except Exception as e:
        print(f"Test Failed: {e}")
        exit(1)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
