
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_ui_login_and_search():
    options = Options()
    options.headless = True
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get('https://your-cep-portal-url.com')
    time.sleep(5)

    try:
        # Wait and input username
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='okta-signin-username']"))
        ).send_keys('FRauto_beta1')
        time.sleep(3)

        # Input password
        driver.find_element(By.XPATH, "//input[@id='okta-signin-password']").send_keys('1@Loveingram12')
        time.sleep(3)

        # Click Login
        driver.find_element(By.XPATH, "//input[@id='okta-signin-submit']").click()
        time.sleep(5)

        # Click 'My Business'
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[2]/div[1]/svg[contains(@class,'MuiSvgIcon-fontSizeMedium MuiSvgIcon-root')]"))
        ).click()
        time.sleep(3)

        # Click 'Invoices' link
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Mes factures / Mes avoirs')]"))
        ).click()
        time.sleep(5)

        # Search for Invoice number
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=':r4v:']"))
        ).send_keys('217178006')
        time.sleep(3)

        # Click Search
        search_icon = driver.find_element(By.XPATH, "//button[@type='submit']")
        search_icon.click()
        time.sleep(5)

        # Validate search result
        if "217178006" in driver.page_source:
            print("Test Passed")
            exit(0)
        else:
            print("Test Failed: No results found")
            exit(1)

    except Exception as e:
        print(f"Test Failed: {e}")
        exit(1)

    finally:
        driver.quit()

test_ui_login_and_search()
