from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com/upload")

# File upload
upload_element = driver.find_element("id", "fileUpload")
upload_element.send_keys("/path/to/file.txt")

driver.quit()
