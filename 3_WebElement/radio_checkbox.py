# Registration Test Case
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# launch Browser
driver = webdriver.Chrome()
driver.maximize_window()

# open website
driver.get("https://automationexercise.com/")


# verify Sign up/Login visible and click on it
signup = driver.find_element(By.LINK_TEXT, "Signup / Login")
try:
    assert signup.is_displayed(), f"Signup / Login not Visible, Test Failed."
    print("Signup / Login Visible. Test Passed.")
    # click on Products
    signup.click()
    print("Signup / Login Visible. Clicked Successfully.")
except Exception as e:
    print("Exception:", e)

# Verify Name is visible and enable then Enter Name
name = driver.find_element(By.CSS_SELECTOR, "[type='text']")
try:
    assert name.is_displayed(), f"---Name not Visible, Test Failed.---"
    print("---Name Visible. Test Passed.---")
    try:
        assert name.is_enabled(), f"Name not Enabled, Test Failed."
        print("---Name Enabled. Test Passed.---")
        # Enter Name
        name.send_keys("Superman")
        print("Name Typed Successfully.")
    except Exception as e:
        print("Exception:", e)
except Exception as e:
    print("Exception:", e)

# Verify Email address is visible and enable then Enter Name
email = driver.find_element(By.CSS_SELECTOR, ".signup-form > form[method='post'] > input[name='email']")
try:
    assert email.is_displayed(), f"---Email not Visible, Test Failed.---"
    print("---Email Visible. Test Passed.---")
    try:
        assert email.is_enabled(), f"Email not Enabled, Test Failed."
        print("---Email Enabled. Test Passed.---")
        # Enter Email
        email.send_keys("Superman@gmail.com")
        print("Email typed Successfully.")
    except Exception as e:
        print("Exception:", e)
except Exception as e:
    print("Exception:", e)

# Verify Signup button is visible and click on it
signup_button = driver.find_element(By.CSS_SELECTOR, ".signup-form > form[method='post'] > .btn.btn-default")
try:
    assert signup_button.is_displayed(), f"Signup Button not Visible, Test Failed."
    print("---Signup Box Button Visible. Test Passed.---")
    # click on search box button
    signup_button.click()
    print("Signup button Clicked Successfully.")
except Exception as e:
    print("Exception:", e)


# Verify Title is visible and click on it
title = driver.find_element(By.CSS_SELECTOR, "[action] .radio-inline:nth-child(3) [type]")
try:
    assert title.is_displayed(), f"---Title Visible, Test Failed.---"
    print("---Title Visible. Test Passed.---")
    # click on search box button
    title.click()
    print("Title Clicked Successfully.")
except Exception as e:
    print("Exception:", e)

# Verify Newsletter is visible and click on it
news_letter = driver.find_element(By.CSS_SELECTOR, "input#newsletter")
try:
    assert news_letter.is_displayed(), f"---Newsletter Visible, Test Failed.---"
    print("---Newsletter Visible. Test Passed.---")
    # click on search box button
    news_letter.click()
    print("NewsLetter Clicked Successfully.")
except Exception as e:
    print("Exception:", e)

time.sleep(10)