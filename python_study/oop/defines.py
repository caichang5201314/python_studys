"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/14 9:18
@desciption: 类的定义和调用
"""


# 定义
class Person():
    # 属性
    name = ''
    age = 0
    sex = ''
    family = []

    # 方法
    def eat(self):
        print('人吃...')

    def sleep(self):
        print('人睡....')

    def play(self, name):
        print(f'我玩的是{name}')


fengjie = Person()  # fengjie是Person类的对象,fengjie对Person做了实例化操作,fengjie我们也叫对象

# 想用类中的属性和方法,一定要先实例化一个对象出来才能通过对象.
# 那这种一切都通过对象来处理的编程思想:面向对象编程
fengjie.name = '凤姐'
fengjie.sex = '女'

print(fengjie.name)
fengjie.eat()
fengjie.play('水')
