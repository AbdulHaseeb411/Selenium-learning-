from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Working with cookies
driver.add_cookie({"name": "myCookie", "value": "cookieValue"})
cookies = driver.get_cookies()

driver.quit()
