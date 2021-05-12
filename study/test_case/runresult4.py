import unittest

from study.test_case import runresult2
from study.test_case import runresult3

""" 
方式四：嵌套测试套件（多个测试套件构建成更大的测试套件） 
"""
suite1 = runresult2.suite()
suite2 = runresult3.suite()
alltests = unittest.TestSuite([suite1, suite2])

runner = unittest.TextTestRunner()
runner.run(alltests)
