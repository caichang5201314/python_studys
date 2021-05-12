import unittest

from study.test_case.test_Demo1 import TestDemo1

""" 
方式三：定义函数（map方式添加用例） 
"""


def suite():
    tests = ['test_case1', 'test_case2']
    return unittest.TestSuite(map(TestDemo1, tests))


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
