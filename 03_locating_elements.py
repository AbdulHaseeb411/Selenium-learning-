from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Locate elements using different selectors
element_by_id = driver.find_element("id", "exampleId")
element_by_class = driver.find_element("class name", "exampleClass")
element_by_name = driver.find_element("name", "exampleName")

driver.quit()
