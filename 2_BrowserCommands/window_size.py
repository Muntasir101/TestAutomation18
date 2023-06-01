from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("https://www.bbc.com")

driver.set_window_size(700, 700)
time.sleep(3)

driver.maximize_window()

driver.quit()  # Closes all windows and terminate WebDriver session.
