from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Click an element
button = driver.find_element(By.ID, "submitButton")
button.click()

# Enter text into an input field
input_field = driver.find_element(By.NAME, "username")
input_field.send_keys("myUsername")

driver.quit()
