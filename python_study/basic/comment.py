"""
@author: 蔡昶
@email: caichangfast@qq.com
@time: 2021/7/12 9:45
@desciption: 注释的用法
    注释的作用就是为了方便其他人能读懂你的程序或你以后维护代码方便而说的'一些话'

    1.整个文档的最开始,声明这个文档的作用
    2.函数或类上用
    3.如果有的行你要注明是什么意思就用注释去解释
"""


# 这是Test类  ctrl+/
# 其中提供了chi这个方法

class Test():
    """这个是吃的方法,用来描述吃的行为"""

    def chi(self):
        name = 'caichang'  # 姓名等于caichang
        print('chi...')
