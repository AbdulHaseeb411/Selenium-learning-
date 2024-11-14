from selenium import webdriver

# Assuming Selenium Grid is running at localhost on port 4444
grid_url = "http://localhost:4444/wd/hub"

# Desired capabilities for Chrome
capabilities = {"browserName": "chrome"}

driver = webdriver.Remote(command_executor=grid_url, desired_capabilities=capabilities)
driver.get("https://www.example.com")

print("Page title:", driver.title)
driver.quit()
