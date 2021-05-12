import unittest

from study.unitest_study.testsuite_test import TestDemo2

""" 
测试套件：方式二：unittest.TestSuite()--addTest()                                    
"""
suite = unittest.TestSuite()
suite.addTest(TestDemo2('test_case_b'))
suite.addTest(TestDemo2('test_case_a'))
runner = unittest.TextTestRunner()
runner.run(suite)
