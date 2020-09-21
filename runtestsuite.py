import HTMLTestRunnerCN
import os
import time
import unittest

#测试单个用例
from testcase.test_location import *
from testcase.test_sql import testmysql
from testcase.test_temperature import MyTests_tempreature

if __name__ == "__main__":

    suite = unittest.TestSuite()
    #指定要执行的用例的类名
    #MyTests_tempreature  MyTests
    uite1 = unittest.TestLoader().loadTestsFromTestCase(MyTests_tempreature)
    suite.addTests(uite1)

    report_dir = './test_report'
    os.makedirs(report_dir, exist_ok=True)
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    report_name = '{0}/{1}.html'.format(report_dir, now)

    with open(report_name, 'wb')as f:
        runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=f,verbosity=2, tester='longhp',title="测试报告", description="本测试报告内容包含app的简单测试")
        runner.run(suite)

