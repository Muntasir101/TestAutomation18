import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_valid():
    # 1. Launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get("http://automationexercise.com")

    # 3. Verify that home page is visible successfully
    try:
        assert "Automation Exercise" in driver.title
        print("Home page is visible successfully.Test passed")
    except Exception as e:
        print(f"home page is not visible successfully, Test Failed.", type(e).__name__)

    # 4. Click on 'Signup / Login' button
    try:
        signup_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(4) > a")))
        assert signup_button.is_displayed()
        print("Signup / Login Visible.Click on 'Signup / Login' button.")
        signup_button.click()
        time.sleep(5)
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

    # 6. Enter correct email address and password
    # Email address
    try:
        email = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".login-form > form[method='post'] > input[name='email']")))
        assert email.is_displayed()
        print("Email is Visible.Enter incorrect email.")
        email.send_keys("y63ca@hotmail.com")
        time.sleep(5)
    except Exception as e:
        print(f"username not Visible.", type(e).__name__)

    # password
    try:
        password = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[type='password']")))
        assert password.is_displayed()
        print("password is Visible.Enter incorrect password")
        password.send_keys("0123456789")
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

    # 8. Verify that 'Logged in as username' is visible
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(10) > a")))

        assert "Logged in as " in success_message.text
        print("'Logged in as username' visible.Test passed")
    except Exception as e:
        print(f"'Logged in as username' not visible.Test failed.", type(e).__name__)

    driver.quit()


# 9. Click 'Delete Account' button
# 10. Verify that 'ACCOUNT DELETED!' is visible

test_login_valid()
