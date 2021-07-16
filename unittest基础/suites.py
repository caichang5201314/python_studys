import unittest

from unittest基础.demo1 import Mtesting
from unittest基础.demo2 import Caichang

'''
    每轮(每次版本)测试,我就增加一个测试套件
    在这个套件中加入你要测试的测试用例,执行即可
    这样就能说这轮测试到底过关了哪些内容
'''
suite = unittest.TestSuite()
suite.addTest(Mtesting('test_1_two'))
suite.addTest(Caichang('test_baobao'))
suite.addTest(Caichang('test_caichang'))
runner = unittest.TextTestRunner()
runner.run(suite)
