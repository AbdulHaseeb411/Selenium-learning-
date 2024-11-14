from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Example of keyboard action: Selecting text and copying
input_box = driver.find_element("id", "inputField")
input_box.send_keys("Selenium Test")
ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").send_keys("c").key_up(Keys.CONTROL).perform()

# Example of mouse action: Double-clicking
element = driver.find_element("id", "doubleClickElement")
ActionChains(driver).double_click(element).perform()

driver.quit()
