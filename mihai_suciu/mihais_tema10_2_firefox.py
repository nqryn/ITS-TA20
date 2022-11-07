import unittest
import HTMLTestRunner
from magento_firefox.magento_login_page import MagentoLoginTestCase
from magento_firefox.magento_first_page import MagentoFirstPageTestCase   # erori de Assert
from magento_firefox.magento_create_account_page import MagentoCreateAccountTestCase  # erori de Assert
from magento_firefox.magento_whatsnew_page import MagentoWhatsnewPageTestCase


class MagentoTestSuite(unittest.TestCase):

    def test_suite(self):

        my_test_suite = unittest.TestSuite()
        my_test_suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(MagentoLoginTestCase),
            unittest.defaultTestLoader.loadTestsFromTestCase(MagentoFirstPageTestCase),
            unittest.defaultTestLoader.loadTestsFromTestCase(MagentoCreateAccountTestCase),
            unittest.defaultTestLoader.loadTestsFromTestCase(MagentoWhatsnewPageTestCase),
        ])

        test_runner = HTMLTestRunner.HTMLTestRunner(
            title='magento_firefox Test Report',
            report_name='ITF - Tema 10',
            description='Firefox - HTMLTestRunner',
            tested_by="Mihai Suciu",
            open_in_browser=True
        )

        test_runner.run(my_test_suite)
