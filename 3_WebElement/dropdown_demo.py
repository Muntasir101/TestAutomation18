import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def dropdown_select():
    # launch Browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # open website
    driver.get("https://the-internet.herokuapp.com/dropdown")

    try:
        dropdown = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "select#dropdown")))
        assert dropdown.is_displayed(), f"dropdown not Visible, Test Failed."
        print("dropdown Visible. Test Passed.")

        dropdown_options = Select(dropdown)
        #dropdown_options.select_by_value("1")
        #dropdown_options.select_by_visible_text("Option 2")
        dropdown_options.select_by_index(1)
        time.sleep(5)
    except Exception as e:
        print("Exception Type:", type(e).__name__)


dropdown_select()
