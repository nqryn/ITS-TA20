import unittest
import HtmlTestRunner
from sauce_demo_test import SauceDemoTestCase
from selenium_site_test import SeleniumEasyTest





class ClassaDeTest(unittest.TestCase):

    def test_suit(self):
        my_test_suit = unittest.TestSuite()
        my_test_suit.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(SauceDemoTestCase),
            unittest.defaultTestLoader.loadTestsFromTestCase(SeleniumEasyTest)
        ])

        test_runnner = HtmlTestRunner.HTMLTestRunner(
            report_title="Primul214 report",
            report_name="Test Proiect Final213413241"
        )

        test_runnner.run(my_test_suit)

