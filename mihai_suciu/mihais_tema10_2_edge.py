import unittest
import HtmlTestRunner
from Magento.magento_login_page import MagentoLoginTestCase
from Magento.magento_first_page import MagentoFirstPageTestCase   # erori de Assert(try-except)
from Magento.magento_create_account_page import MagentoCreateAccountTestCase  # erori de Assert(try-except)
from Magento.magento_whatsnew_page import MagentoWhatsnewPageTestCase


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
            report_name="Edge Report",
            combine_reports=True
        )

        test_runner.run(my_test_suite)
