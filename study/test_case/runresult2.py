import unittest

""" 
方式二：定义函数 
"""


def suite():
    test_dir = '/'  # ./test_case为根目录下的文件夹路径
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    return discover


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
