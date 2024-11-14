from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Take a screenshot
driver.save_screenshot("screenshot.png")

driver.quit()
