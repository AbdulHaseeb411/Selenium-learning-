from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Switch to iframe and interact with elements inside
driver.switch_to.frame("iframeName")
iframe_element = driver.find_element("id", "insideIframeElement")

driver.switch_to.default_content()
driver.quit()
