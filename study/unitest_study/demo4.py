import unittest

""" 
跳过测试（跳过类） 
"""


class TestDemo1(unittest.TestCase):
    def test_case1(self):
        print('test_case1')

    def test_case2(self):
        print('test_case2')


@unittest.skip('跳过测试类TestDemo2')
class TestDemo2(unittest.TestCase):
    def test_case3(self):
        print('test_case3')

    def test_case4(self):
        print('test_case4')


if __name__ == '__main__':
    unittest.main(verbosity=2)
