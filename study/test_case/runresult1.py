"""
测试套件：方式二：unittest.TestSuite()--addTest()
"""
import unittest

from study.test_case.test_Demo1 import TestDemo1
from study.test_case.test_Demo2 import TestDemo2

suite = unittest.TestSuite()
suite.addTest(TestDemo1('test_case1'))
suite.addTest(TestDemo1('test_case2'))
suite.addTest(TestDemo2('test_case20'))
runner = unittest.TextTestRunner()
runner.run(suite)