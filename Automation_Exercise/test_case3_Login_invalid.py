import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_invalid():
    # 1. Launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get("http://automationexercise.com")

    # 3. Verify that home page is visible successfully
    try:
        assert "Automation Exercise" in driver.title
        print("home page is visible successfully.Test passed")
    except Exception as e:
        print(f"home page is not visible successfully, Test Failed.", type(e).__name__)

    # 4. Click on 'Signup / Login' button
    try:
        signup_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(4) > a")))
        assert signup_button.is_displayed()
        print("Signup / Login Visible.Click on 'Signup / Login' button.")
        signup_button.click()
    except Exception as e:
        print(f"Signup / Login not Visible, Test Failed.", type(e).__name__)

    # 5. Verify 'Login to your account' is visible
    try:
        login_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".login-form > h2")))

        assert "Login to your account" in login_element.text
        print("Login to your account' is visible.Test passed")
    except Exception as e:
        print(f"Login to your account' is not visible, Test Failed.", type(e).__name__)

    # 6. Enter incorrect email address and password
    # Email address
    try:
        email = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".login-form > form[method='post'] > input[name='email']")))
        assert email.is_displayed()
        print("Email is Visible.Enter incorrect email.")
        email.send_keys("invalid@mail.com")
        time.sleep(5)
    except Exception as e:
        print(f"username not Visible.", type(e).__name__)

    # password
    try:
        password = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[type='password']")))
        assert password.is_displayed()
        print("password is Visible.Enter incorrect password")
        password.send_keys("3231321")
    except Exception as e:
        print(f"password not Visible.", type(e).__name__)

    # 7. Click 'login' button
    try:
        login_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".login-form > form[method='post'] > .btn.btn-default")))
        assert login_button.is_displayed()
        print("Login Button Visible.Click 'login' button")
        login_button.click()
    except Exception as e:
        print(f"Login Button not Visible, Test Failed.", type(e).__name__)

    # 8. Verify error 'Your email or password is incorrect!' is visible
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".login-form > form[method='post'] > p")))

        assert "Your email or password is incorrect!" in error_message.text
        print("'Your email or password is incorrect!t' visible.Test passed")
    except Exception as e:
        print(f"'Your email or password is incorrect!' is not visible, Test Failed.", type(e).__name__)

    driver.quit()


test_login_invalid()
