import unittest
import HtmlTestRunner
from magento_chrome.magento_login_page import MagentoLoginTestCase
from magento_chrome.magento_first_page import MagentoFirstPageTestCase   # erori de Assert(try-except)
from magento_chrome.magento_create_account_page import MagentoCreateAccountTestCase  # erori de Assert(try-except)
from magento_chrome.magento_whatsnew_page import MagentoWhatsnewPageTestCase


class MagentoTestSuite(unittest.TestCase):

    def test_suite(self):

        my_test_suite = unittest.TestSuite()
        my_test_suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(MagentoLoginTestCase),
            unittest.defaultTestLoader.loadTestsFromTestCase(MagentoFirstPageTestCase),
            unittest.defaultTestLoader.loadTestsFromTestCase(MagentoCreateAccountTestCase),
            unittest.defaultTestLoader.loadTestsFromTestCase(MagentoWhatsnewPageTestCase),
        ])

        test_runner = HtmlTestRunner.HTMLTestRunner(
            report_title="Magento Report",
            report_name="Chrome Report",
            combine_reports=True
        )

        test_runner.run(my_test_suite)
