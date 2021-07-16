"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/14 14:00
@desciption: _和__
_:可以简单理解为这个属性或方法有特殊含义,可以掉用,但不推荐调用,有点像java中的受保护(protected)
__:私有的,不对外提供对象调用方式
"""

class Person():
    def __init__(self):
        self.name=''
        self._sex='男'
        self._age=0
        self.__girlfriend='布兰妮'

    def chi(self):
        print('chi....')
        print(f'我的女友是:{self.__girlfriend}')

    def _wan(self):
        print('wan....')
        self.__le()

    def __le(self):
        print('hehe')

cai = Person()
print(cai._sex)
print(cai._age)
cai._wan()
#print(cai.__girlfriend)
cai.chi()
#cai.le()