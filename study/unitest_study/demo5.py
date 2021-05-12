import unittest

""" 
跳过测试：TestCase.skipTest()方法 
"""


class TestDmeo(unittest.TestCase):
    def test_case1(self):
        print('test_case1')
        # TestCase.skipTest()方法
    @unittest.skip('跳过')
    def test_case2(self):
        print('test_case2')


if __name__ == '__main__':
    unittest.main()
