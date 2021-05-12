import unittest

""" 
测试套件：方式二：unittest.TestSuite() 
"""


class TestDemo2(unittest.TestCase):
    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDowm')

    def test_case_a(self):
        print('------------test_case_a---------')

    def test_case_b(self):
        print('------------test_case_b---------')

    def test_case_c(self):
        print('------------test_case_c----------')


if __name__ == '__main__':
    unittest.main()
