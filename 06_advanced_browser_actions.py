from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Right-click and double-click actions
element = driver.find_element("id", "elementId")
actions = ActionChains(driver)
actions.context_click(element).double_click(element).perform()

driver.quit()
