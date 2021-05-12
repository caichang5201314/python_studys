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
        self.assertEqual(1 + 1, 2, '用例失败')

    @unittest.skip('跳过用例test_case2')
    def test_case2(self):
        print('test_case2')
        self.assertEqual(1 + 1, 3, '用例失败')

    @unittest.skipIf(0 > 1, '不跳过用例test_case3')
    def test_case3(self):
        print('test_case3')

    def test_case4(self):
        print('test_case4')


    # skipUnless当condition为False是跳过
    @unittest.skipUnless(0 > 1, '跳过用例test_case5')
    def test_case5(self):
        print('test_case5')


    # skipUnless当condition为False是跳过
    @unittest.skipUnless(0 < 1, '不跳过用例test_case6')
    def test_case6(self):
        print('test_case6')


    # 测试标记为失败
    @unittest.expectedFailure
    def test_case7(self):
        print('test_case7')


if __name__ == '__main__':
    unittest.main(verbosity=2)
