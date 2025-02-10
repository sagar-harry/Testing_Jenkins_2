
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def login(self, driver, username, password):
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def run_test():
    url = "https://saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popups")
    chrome_options.add_argument("--incognito")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(5)
    driver.maximize_window()

    try:
        login_page = LoginPage()
        login_page.login(driver, username, password)
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        ).click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        ).click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a'))
        ).click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]'))
        ).click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))
        ).send_keys("somename")
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        time.sleep(3)

        payment_info_visible = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'))
        )

        if payment_info_visible:
            print("Payment Information is visible. Test Passed.")
            exit(0)

    except Exception as e:
        print(f"Test Failed: {e}")
        exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
