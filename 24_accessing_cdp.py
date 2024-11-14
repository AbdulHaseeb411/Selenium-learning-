from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Enable Chrome DevTools Protocol (CDP)
options = Options()
options.add_argument("--auto-open-devtools-for-tabs")

driver = webdriver.Chrome(options=options)
driver.get("https://www.example.com")

# Use CDP to capture performance metrics
driver.execute_cdp_cmd("Network.enable", {})
response = driver.execute_cdp_cmd("Network.getAllCookies", {})
print("Cookies:", response)

driver.quit()
