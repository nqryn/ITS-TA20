import unittest
import HtmlTestRunner

from sauce_demo_test import SauceDemoTestCase
from selenium_easy_test import SeleniumEasyTest


class ClassaDeTest(unittest.TestCase):

    def test_suit(self):
        my_test_suit = unittest.TestSuite()
        my_test_suit.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(SauceDemoTestCase),
            unittest.defaultTestLoader.loadTestsFromTestCase(SeleniumEasyTest)
        ])

        test_runnner = HtmlTestRunner.HTMLTestRunner(
            report_title="Raport Proiect Final",
            report_name="Test Proiect Final"
        )

        test_runnner.run(my_test_suit)