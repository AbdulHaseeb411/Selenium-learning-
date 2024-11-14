from selenium import webdriver

# Setup: Initialize the WebDriver
driver = webdriver.Chrome()  # or webdriver.Firefox() if using Firefox

# Open a webpage
driver.get("https://www.example.com")

# Close the browser
driver.quit()
