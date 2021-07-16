"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/14 10:24
@desciption: 方法
方法：同属性
    1.普通方法：通过对象.调用   (常用)
    2.静态方法：既可对象.也可类名. ,方法上加入@staticmethod,同时取消self (不常用)

补充:类方法
类方法:用@classmethod修饰的方法,同时他多一个cls,这个cls就是指类名

玩面向对象的普通方法,其实和面向过程的函数是一模一样的,只是多一个self(对象的影子)

"""

class Person():
    name='caichang'
    #普通方法
    def chi(self):
        print('chi....')
    def wan(self):
        print('wan.....')

    @staticmethod
    def le():
        print('le.....')

    @classmethod
    def he(cls):
        print(f'he.....{cls.name}')

    def two(self,start,end,step=1):
        result = []
        for i in range(start,end,step):
            if i % 3 == 0 and i % 5 != 0:
                result.append(i)
        print(f'结果为:{result}')

cai = Person()
cai.chi()

Person.le()
cai.le()

Person.he()

cai.two(1,50)