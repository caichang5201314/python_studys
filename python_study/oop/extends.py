"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/14 14:21
@desciption: 继承
目的:少写代码
1.在class 类名(继承类): 其中继承类可以写多个,从而实现多继承
2.通过super掉父类的方法
3.如果子类的方法和父类方式一致,就意味着:子类复写了父类
"""


class Animal():
    def __init__(self):
        self.name = ''
        self.age = 0
        self.height = 1

    def sleep(self):
        print('动物睡')


class Bird():
    def fly(self):
        print('鸟飞.....')

    def sleep(self):
        print('鸟睡.....')


class Cat(Animal, Bird):
    # 子类复写了父类的方法,(override)
    def fly(self):
        # 通过super可调用父类的方法
        super().fly()
        print('猫咪也疯狂,我也会飞....')


jiafei = Cat()
print(jiafei.name)
jiafei.sleep()
jiafei.fly()

