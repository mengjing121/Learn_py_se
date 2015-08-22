import unittest
from testProduct1 import productTest1
from testProduct2 import productTest2
import os
import HTMLTestRunner

search_test1 = unittest.TestLoader().loadTestsFromTestCase(productTest1)
search_test2 = unittest.TestLoader().loadTestsFromTestCase(productTest2)

suite = unittest.TestSuite([search_test1,search_test2])

#unittest.TextTestRunner().run(suite)

output_file = open("D:\Selenium\Learning\SmokeTestReport.html",'w')

runner = HTMLTestRunner.HTMLTestRunner(
	stream=output_file,
	title='Test Report',
	description='Smoke Tests')

runner.run(suite)