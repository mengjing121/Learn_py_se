from selenium import webdriver
import unittest
from __builtin__ import classmethod

class productTest1(unittest.TestCase):
	@classmethod
	def setUp(cls):
		cls.driver = webdriver.Chrome()
		cls.driver.get("http://demo.magentocommerce.com/")

	def test_search_product(self):
		self.search_field = self.driver.find_element_by_id("search")
		self.search_field.send_keys("phone")
		self.search_field.submit()

		self.products = self.driver.find_elements_by_css_selector(".product-name a")
		#print(self.products)
		self.assertEqual(2, len(self.products))

	def test_search_another_product(self):
		self.search_field = self.driver.find_element_by_id("search")
		self.search_field.send_keys("sale")
		self.search_field.submit()

		result = self.driver.find_element_by_css_selector(".note-msg").text
		self.assertEqual("Your search returns no results.", result)

	@classmethod
	def tearDown(cls):
		cls.driver.quit()

if __name__ == "__main__":
	unittest.main()