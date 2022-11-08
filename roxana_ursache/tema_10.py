# 1. Faceti o suita care sa contina testele voastre de la tema 9 + testele de la
# intalnirea 10 (care au clasa). Generati raportul

import unittest
import HtmlTestRunner

from roxana_ursache.tema_9 import HerokuappLoginTestCase
from curs.sesiunea10_extra.alerts import AlertTests

class MyTestSuite(unittest.TestCase):

    def test_suite(self):
        my_test_suite = unittest.TestSuite()
        my_test_suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(HerokuappLoginTestCase),
            unittest.defaultTestLoader.loadTestsFromTestCase(AlertTests)
        ])

        test_runner = HtmlTestRunner.HTMLTestRunner(
            report_title="My first report",
            report_name="tema10_report",
            combine_reports=True
        )
        test_runner.run(my_test_suite)