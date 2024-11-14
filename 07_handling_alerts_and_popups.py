from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Handling an alert
alert = driver.switch_to.alert
alert.accept()  # or alert.dismiss()

driver.quit()
