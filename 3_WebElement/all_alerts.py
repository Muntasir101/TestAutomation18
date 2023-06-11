import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By


def handle_alert():
    # launch Browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # open website
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # Normal Alert
    try:
        normal_alert = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(1) > button")))
        assert normal_alert.is_displayed(), f"normal_alert not Visible, Test Failed."
        print("normal_alert Visible. Test Passed.")
        time.sleep(5)

        try:
            normal_alert.click()
            time.sleep(3)
            normal_alert_present = WebDriverWait(driver, 10).until(EC.alert_is_present())
            driver.switch_to.alert.accept()
            time.sleep(3)
        except Exception as e:
            print("Exception Type:", type(e).__name__)
            print("No Normal Alert present.test Failed.")

    except Exception as e:
        print("Exception Type:", type(e).__name__)

    # Confirmation Alert
    try:
        confirmation_alert = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(2) > button")))
        assert confirmation_alert.is_displayed(), f"confirmation_alert not Visible, Test Failed."
        print("confirmation_alert Visible. Test Passed.")
        time.sleep(5)

        try:
            confirmation_alert.click()
            time.sleep(3)
            confirmation_alert_present = WebDriverWait(driver, 10).until(EC.alert_is_present())
            driver.switch_to.alert.dismiss()
            time.sleep(3)
        except Exception as e:
            print("Exception Type:", type(e).__name__)
            print("No Confirmation Alert present.test Failed.")

    except Exception as e:
        print("Exception Type:", type(e).__name__)

    # Prompt Alert
    try:
        prompt_alert = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(3) > button")))
        assert prompt_alert.is_displayed(), f"prompt_alert not Visible, Test Failed."
        print("prompt_alert Visible. Test Passed.")
        time.sleep(5)

        try:
            prompt_alert.click()
            time.sleep(3)
            prompt_alert_present = WebDriverWait(driver, 10).until(EC.alert_is_present())
            driver.switch_to.alert.send_keys("Test Automation by Selenium.")
            driver.switch_to.alert.accept()
            time.sleep(3)
        except Exception as e:
            print("Exception Type:", type(e).__name__)
            print("No Prompt Alert present.test Failed.")

    except Exception as e:
        print("Exception Type:", type(e).__name__)

    driver.quit()


handle_alert()
