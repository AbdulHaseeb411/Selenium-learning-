from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Setup options and capabilities
options = Options()
options.add_argument("--incognito")
options.add_argument("--disable-popup-blocking")

# Add a proxy setting as an example capability
capabilities = webdriver.DesiredCapabilities.CHROME.copy()
capabilities['proxy'] = {
    "proxyType": "MANUAL",
    "httpProxy": "http://127.0.0.1:8080"
}

driver = webdriver.Chrome(options=options, desired_capabilities=capabilities)
driver.get("https://www.example.com")

print("Page title:", driver.title)
driver.quit()
