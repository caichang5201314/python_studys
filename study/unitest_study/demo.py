import unittest

""" 
基本示例 
"""


# 定义测试类，父类为unittest.TestCase
class TestDemo(unittest.TestCase):
    # 必须使用@classmethod装饰器，所有test运行前执行一次
    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    # 必须使用@classmethod装饰器，所有test运行完后执行一次
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    # 每个测试方法运行前执行
    def setUp(self):
        print('setUp')

    # 每个测试方法运行后执行
    def tearDown(self):
        print('tearDowm')

    # 所有的测试方法都要以test为开头
    def test_case1(self):
        print('test_case1')

    def test_case2(self):
        print('test_case2')

    def test_case3(self):
        print('test_case3')

    def test_case4(self):
        print('test_case4')


if __name__ == '__main__':
    unittest.main(verbosity=2)
