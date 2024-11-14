import unittest
from selenium import webdriver

class TestExample(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_title(self):
        self.driver.get("https://www.example.com")
        self.assertIn("Example", self.driver.title)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
