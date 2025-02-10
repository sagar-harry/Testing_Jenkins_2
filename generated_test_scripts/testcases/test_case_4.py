
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_ui():
    options = Options()
    options.headless = True
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)

    try:
        driver.maximize_window()
        driver.get("http://example.com")
        time.sleep(5)

        locator = (By.XPATH, "fnan")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
        time.sleep(3)

        element = driver.find_element(*locator)
        # Additional actions can be added here.
        # Example: element.click()
        time.sleep(3)

        print("Test case passed")
        sys.exit(0)

    except Exception as e:
        print(f"Test case failed with exception: {e}")
        sys.exit(1)

    finally:
        driver.quit()

test_ui()
