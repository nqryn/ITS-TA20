import unittest

import HtmlTestRunner

from curs.sesiunea9_verificari.test_unit import MyFirstTestCase, JulesTestCase


class MyFirstTestSuite(unittest.TestCase):

    def test_suite(self):
        # Facem un obiect din clasa TestSuite
        my_test_suite = unittest.TestSuite()
        # In acest obiect, adaugam (prin load) testele din toate clasele
        # pe care vrem sa le rulam
        my_test_suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(MyFirstTestCase),
            unittest.defaultTestLoader.loadTestsFromTestCase(JulesTestCase)
        ])

        # Facem un test runner HTML, care va genera pentru noi niste rapoarte
        # human-friendly pentru toate testele rulate
        test_runner = HtmlTestRunner.HTMLTestRunner(
            report_title="My first report",
            report_name="sesiunea10_report",
            combine_reports=True
        )
        # La final, ii zicem runner-ului sa ruleze intreaga suita de teste
        test_runner.run(my_test_suite)
