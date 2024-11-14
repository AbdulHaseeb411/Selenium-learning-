from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--auto-open-devtools-for-tabs")

driver = webdriver.Chrome(options=options)
driver.get("https://www.example.com")

# Access network logs
logs = driver.get_log("performance")
for entry in logs:
    print(entry)

driver.quit()
