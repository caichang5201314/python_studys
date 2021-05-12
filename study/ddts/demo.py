import unittest
import ddt

test_data = [
    {"username": "abcd", "password": "1234", "expect": True},
    {"username": "asdf", "password": "3456", "expect": False},
    {"username": "qwer", "password": "5432", "expect": True}
]


@ddt.ddt
class TestDemo2(unittest.TestCase):
    def setUp(self):
        print("测试开始")

    def tearDown(self):
        print("测试结束")

    @ddt.data(*test_data)
    def testCase01(self, data):
        '''''测试用例01'''
        print(data["username"] + data["password"] + str(data["expect"]))


if __name__ == '__main__':
    unittest.main()
