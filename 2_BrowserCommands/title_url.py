from selenium import webdriver

# launch Browser
driver = webdriver.Firefox()

# open website
driver.get("https://www.bbc.com")

# Get current Title
get_title = driver.title
print("Title:", get_title)

# verify title
try:
    expected_title = "BBC - Homepage"
    assert expected_title == driver.title, f"Title mismatch"
    print("Title Verified.")
except Exception as e:
    print("Exception:", e)

# Get current URL
get_url = driver.current_url
print("URL:", get_url)

# url verification
expected_url = "https://www.bbc.com/"
try:
    assert expected_url == driver.current_url, f"URL mismatch"
    print("URL Verified.")
except Exception as e:
    print("Exception:", e)

# close browser
driver.close()  # Closes only the current window or tab
