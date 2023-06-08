"""
Wait for a specified amount of time for an element to appear before
throwing a NoSuchElementException.
Implicit wait can be helpful when there are certain element on page that
take varying amounts of time.
This is global wait time that is applied to all elements.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


def implicit_wait_real_implementation():
    # launch Browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # open website
    driver.get("https://automationexercise.com/")

    # set an implicit wait
    driver.implicitly_wait(20)

    # verify Products visible and click on it; wrong locator
    products = driver.find_element(By.CSS_SELECTOR, "a[href='/products22']")
    try:
        assert products.is_displayed(), f"Products not Visible, Test Failed."
        print("Products Visible. Test Passed.")
        # click on Products
        products.click()
    except Exception as e:
        print("Exception:", e)

    driver.quit()


implicit_wait_real_implementation()
