from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Enable mobile emulation
mobile_emulation = {"deviceName": "iPhone X"}
options = Options()
options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(options=options)
driver.get("https://www.example.com")

# Check page title
print("Page title:", driver.title)
driver.quit()
