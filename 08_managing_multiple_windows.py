from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Open a new window and switch
driver.execute_script("window.open('https://www.google.com', '_blank');")
driver.switch_to.window(driver.window_handles[1])

driver.quit()
