"""
Explicit wait are used to wait for a certain condition to occur
before proceeding with the execution of the next step.
We can specify maximum amount of time to wait and condition to wait for.
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

wait = WebDriverWait(driver, 10)

"""
# verify Products visible and click on it: apply explicit wait- visibility_0f_element_located
try:
    products = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/products22']")))
    assert products.is_displayed(), f"Products not Visible, Test Failed."
    print("Products Visible. Test Passed.")
    # click on Products
    products.click()
except Exception as e:
    print("Exception Type:", type(e).__name__)
    
# output: Exception Type: TimeoutException
"""

"""
# verify Products visible and click on it: apply explicit wait - presence_of_element_located
try:
    products = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/products22']")))
    assert products.is_displayed(), f"Products not Visible, Test Failed."
    print("Products Visible. Test Passed.")
    # click on Products
    products.click()
except Exception as e:
    print("Exception Type:", type(e).__name__)

# output: Exception Type: TimeoutException
"""

# Verify Title by using title_contains
try:
    expected_title = "Automation Exercise"
    assert wait.until(EC.title_contains(expected_title))
    print("Title Verified.")
except Exception as e:
    print("Title Exception Type:", type(e).__name__)

# verify URL by using
try:
    assert wait.until(EC.url_to_be("https://automationexercise.com/"))
    print("URL Verified.")
except Exception as e:
    print("URL Exception Type:", type(e).__name__)

# Text verify
try:
    products_text = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "a[href='/products']"), "Products"))
    print("Product Text Verified.")
except Exception as e:
    print("Text Exception Type:", type(e).__name__)

driver.quit()
