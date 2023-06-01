from selenium import webdriver

# launch Browser
driver = webdriver.Firefox()

# open website
driver.get("https://www.google.com")

# close browser
driver.close()
