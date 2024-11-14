from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Extract and parse data
title = driver.find_element("tag name", "h1").text
print("Page title:", title)

driver.quit()
