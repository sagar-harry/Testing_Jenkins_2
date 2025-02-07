
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def check_payment_information():
    driver = setup_driver()
    driver.get('http://example.com')  # Use your actual URL
    time.sleep(5)
    driver.maximize_window()

    try:
        login_page = LoginPage(driver)
        login_page.login('your-username', 'your-password')
        
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('somename')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('lastname')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('123456')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        time.sleep(3)

        payment_info_visible = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]').is_displayed()

        if payment_info_visible:
            print("Test Passed")
            driver.quit()
            exit(0)
        else:
            print("Test Failed")
            driver.quit()
            exit(1)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        driver.quit()
        exit(1)

check_payment_information()
