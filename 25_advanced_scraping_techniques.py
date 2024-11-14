from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Handling pagination or infinite scroll
while True:
    try:
        load_more_button = driver.find_element(By.ID, "loadMore")
        load_more_button.click()
        time.sleep(2)
    except Exception as e:
        print("Reached end of page or button not found:", e)
        break

# Scrape content after loading
elements = driver.find_elements(By.CLASS_NAME, "dataItem")
for element in elements:
    print(element.text)

driver.quit()
