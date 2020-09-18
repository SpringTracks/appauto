import os
import time
import unittest
import logging
import HTMLTestRunnerCN
from HTMLTestRunner_cn import HTMLTestRunner

#执行所有testcase下test开头的用例
test_dir = './testcase'
discover = unittest.defaultTestLoader.discover(start_dir='./testcase', pattern="test*.py")

if __name__ == "__main__":
    report_dir = './test_report'
    os.makedirs(report_dir, exist_ok=True)
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    report_name = '{0}/{1}.html'.format(report_dir, now)
    #logging.basicConfig(filename='./log/%s.log' %(now), level=logging.INFO)

    with open(report_name, 'wb')as f:
        runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=f,verbosity=2, tester='longhp',title="测试报告", description="本测试报告内容包含app的简单测试")
        #runner = HTMLTestRunner(verbosity=2, title="测试报告", description="本测试报告内容包含app的简单测试",retry=1, save_last_try=True)
        runner.run(discover)

