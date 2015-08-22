from selenium import webdriver
import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from __builtin__ import classmethod

class productTest2(unittest.TestCase):
	@classmethod
	def setUp(cls):
		cls.driver = webdriver.Chrome()
		cls.driver.get("http://demo.magentocommerce.com/")

	def test_search_field(self):
		self.assertTrue(self.element_is_present(By.ID,"search"))

	@classmethod
	def tearDown(cls):
		cls.driver.quit()

	def element_is_present(self,type,locator):
		try:
			self.driver.find_element(type,locator)
		except NoSuchElementException, e:
			return False
		return True

if __name__ == "__main__":
	unittest.main()