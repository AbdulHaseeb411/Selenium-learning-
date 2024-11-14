from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
import time

driver = webdriver.Chrome()
driver.get("https://www.example.com")

try:
    element = driver.find_element("id", "dynamicElement")
    time.sleep(5)  # Wait for page to reload content
    element.click()  # Attempt click again
except StaleElementReferenceException:
    print("StaleElementReferenceException caught. Refinding element...")
    element = driver.find_element("id", "dynamicElement")
    element.click()

driver.quit()
