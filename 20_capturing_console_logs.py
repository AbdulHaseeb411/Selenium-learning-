from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Enable logging
caps = DesiredCapabilities.CHROME.copy()
caps["goog:loggingPrefs"] = {"browser": "ALL"}

driver = webdriver.Chrome(desired_capabilities=caps)
driver.get("https://www.example.com")

# Capture console logs
for entry in driver.get_log("browser"):
    print(entry)

driver.quit()
