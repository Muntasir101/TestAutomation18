# Automate Product Search Test Case
from selenium import webdriver
from selenium.webdriver.common.by import By

# launch Browser
driver = webdriver.Chrome()

# open website
driver.get("https://automationexercise.com/")

# verify Products visible and click on it
products = driver.find_element(By.CSS_SELECTOR, "a[href='/products']")
try:
    assert products.is_displayed(), f"Products not Visible, Test Failed."
    print("Products Visible. Test Passed.")
    # click on Products
    products.click()
except Exception as e:
    print("Exception:", e)


# Verify Search box is visible and enable then search for tshirt
search_box = driver.find_element(By.CSS_SELECTOR, "#search_product")
try:
    assert search_box.is_displayed(), f"Search Box not Visible, Test Failed."
    print("Search Box Visible. Test Passed.")
    try:
        assert search_box.is_enabled(), f"Search Box not Enabled, Test Failed."
        print("Search Box Enabled. Test Passed.")
        # Search 'Men Tshirt' on product page
        search_box.send_keys("men tshirt")
    except Exception as e:
        print("Exception:", e)
except Exception as e:
    print("Exception:", e)


# Verify Search box button is visible and click on it
search_box_button = driver.find_element(By.CSS_SELECTOR, "#submit_search")
try:
    assert search_box_button.is_displayed(), f"Search Box Button not Visible, Test Failed."
    print("Search Box Button Visible. Test Passed.")
    # click on search box button
    search_box_button.click()
except Exception as e:
    print("Exception:", e)


# Verify Men TShirt visible in search result page
men_tshirt_product2 = driver.find_element(By.CSS_SELECTOR, "a[href='/product_details/2']")

try:
    assert men_tshirt_product2.is_displayed(), f"Men TShirt not visible, Test Failed."
    print("Men TShirt visible. Test Passed.")
except Exception as e:
    print("Exception:", e)

# close test
driver.quit()
