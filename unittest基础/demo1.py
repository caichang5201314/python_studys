'''
单元测试框架:
    java:junit3.x,4.x
    python:unittest,pytest
    php:phpunit

unittest中有4个重要的概念：
    test fixture
    test case
    test suite
    test runner

1.测试用例的方法都应该是test开头,至于要不要test_随便,建议用test_
2.setUp:每个用例开始前都要先执行setUp中的代码
  tearDown:每个用例执行完后都要执行tearDown中的代码
  注意:setUp和tearDown是由用例来决定次数.  用例数=执行次数
3.setUpClass:他是个类方法,在整个用例中执行一次
4.在测试方法后加入数字,来决定执行顺序,如:test_1_one,也可以test1_one均可
5.忽略某个方法
    场景:
        1.我某个方法还没有写清楚,但是又不想通过注释代码的方式(太不好)来不执行代码,于是用这个知识点
        2.在这轮测试中,有的方法可能不需要被执行,于是我在这些方法上加入这个知识点即可.然后下轮测试如何需要
          这个方法了,我就删除掉即可
    使用方法:方法头上加入,注意:如果加在类上,就对整个类生效
        @unittest.skip('这轮测试先不管整个方法')
            其中括号中为忽略的原因,建议写清晰,方便维护
        @unittest.skipIf(0 > 1, '不跳过用例test_case3')
            0>1:条件,实际工作中这个条件没这样简单
            第二个参数为:原因
        @unittest.skipUnless(0 > 1, '跳过用例test_case5')
            如果条件不满足着跳过,相当于是skipIf的反面

6,标记方法直接为失败的用例:
    场景:这个功能有bug,先标记为测试失败,等开发修改好后,我去掉这个标记即可
    使用方法:方法头上加入
        @unittest.expectedFailure


'''

import unittest


class Mtesting(unittest.TestCase):
    name='caichang'
    def setUp(self):
        print('这是每个用例开始前就要做的事!')
        self.assertEqual(1 + 1, 2, '用例失败')

    def tearDown(self):
        print('这是每个用例结束后就要做的事!')


    def test_2_one(self):
        print('第一条用例')

    def test_1_two(self):
        print('第二条用例')

    @unittest.skip('这轮测试先不管整个方法')
    def test_3_three(self):
        print('three')

    @unittest.skipIf(name=='caichang','这轮测试先不管整个方法')
    def test_4_four(self):
        print('方法4')

    @unittest.expectedFailure
    def test_5_five(self):
        print('方法5')

    @classmethod
    def setUpClass(cls):
        print('类开始之前就执行这个方法')

    @classmethod
    def tearDownClass(cls):
        print('类结束之后就执行这个方法')


if __name__ == '__main__':
    unittest.main(verbosity=2)
