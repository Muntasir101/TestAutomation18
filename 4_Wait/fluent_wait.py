"""
Fluent wait provide more flexibility in defining waiting conditions.
It allows pooling frequency and maximum amount of time to wait for.
It can use for dynamic web page.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

# launch Browser
driver = webdriver.Chrome()
driver.maximize_window()

# open website
driver.get("https://automationexercise.com/")

wait = WebDriverWait(driver, 10, poll_frequency=1)

# wrong locator
try:
    products = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/products22']")))
    assert products.is_displayed(), f"Products not Visible, Test Failed."
    print("Products Visible. Test Passed.")
    # click on Products
    products.click()
except Exception as e:
    print("Exception Type:", type(e).__name__)

# correct locator
try:
    products = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/products']")))
    assert products.is_displayed(), f"Products not Visible, Test Failed."
    print("Products Visible. Test Passed.")
    # click on Products
    products.click()
except Exception as e:
    print("Exception Type:", type(e).__name__)

driver.quit()