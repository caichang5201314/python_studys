import unittest

""" 
测试套件：方式三：unittest.defaultTestLoader() 
"""
test_dir = '/'  # ./test_case为根目录下的文件夹路径
discover = unittest.defaultTestLoader.discover(test_dir, pattern='testsuite_test.py')
runner = unittest.TextTestRunner(verbosity=2)
runner.run(discover)
