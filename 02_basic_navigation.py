from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Navigate to another page
driver.get("https://www.google.com")

# Go back and refresh
driver.back()
driver.refresh()

driver.quit()
