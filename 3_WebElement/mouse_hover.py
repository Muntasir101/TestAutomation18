import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


def mouse_action():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demo.opencart.com/")

    try:
        desktop = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Desktops")))
        assert desktop.is_displayed(), f"normal_alert not Visible, Test Failed."
        print("desktop Visible. Test Passed.")

        actions = ActionChains(driver)
        actions.move_to_element(desktop).perform()
        time.sleep(5)

        try:
            mac1 = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Mac (1)")))
            mac1.click()
            time.sleep(3)
        except Exception as e:
            print("Exception Type:", type(e).__name__)
            print("Cant click on Mac (1).test Failed.")

    except Exception as e:
        print("Exception Type:", type(e).__name__)

    driver.quit()


mouse_action()
