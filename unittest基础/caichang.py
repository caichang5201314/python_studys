from BeautifulReport import BeautifulReport
import unittest
import os
import time
from demo1 import Mtesting

current_path = os.getcwd()
report_path = os.path.join(current_path, "report")
now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

# 报告地址&名称
report_title = 'Example报告' + now + ".html"

# 报告描述
desc = '用于展示修改样式后的HTMLTestRunner'

if __name__ == '__main__':
    testsuite = unittest.TestSuite()
    loader=unittest.TestLoader()
    testsuite.addTests(loader.loadTestsFromModule(Mtesting))
    run = BeautifulReport(testsuite)
    run.report(description=desc, filename=report_title, log_path=report_path)