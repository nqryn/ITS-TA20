import unittest
import HTMLTestRunner
from mihais_tema09 import HerokuFormAuthenticationPageTestCase
from mihais_tema09 import HerokuAuthenticationTestCase
from curs.sesiunea10_extra.alerts import AlertTests

class Tema09TestSuite(unittest.TestCase):

    def test_suite(self):

        my_test_suite = unittest.TestSuite()
        my_test_suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(HerokuFormAuthenticationPageTestCase),
            unittest.defaultTestLoader.loadTestsFromTestCase(HerokuAuthenticationTestCase),
            unittest.defaultTestLoader.loadTestsFromTestCase(AlertTests)
        ])

        test_runner = HTMLTestRunner.HTMLTestRunner(
            report_title="Heroku Test",
            report_name="Heroku Authentication Test Case",
            combine_reports=True
            )

        test_runner.run(my_test_suite)
