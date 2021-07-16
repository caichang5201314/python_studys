"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/14 9:45
@desciption: 属性，初始化方法(__init__)
属性：
    1.普通属性:普通属性定义在__init__中,只能通过对象.进行调用    (几乎都用)
    2.静态属性:不放在__init__中,可以通过对象.也可以通过类名.调用  (一般不用)

初始化：
    1.一个类可以有初始化方法也可以没有初始化方法
    2.初始性化方法中一般定义普通属性
    3.初始化方法可以带参也可以不带参，如果带了参，实例化时就必须传参
"""


class Person():
    eye = '黑'  # 静态属性

    def __init__(self,id,sex):
        self.name = ''  # 普通属性
        self.age = 0
        self.id=id
        self.sex=sex


#当我实例化后，一定要立刻看是否有__init__，如果有，一定要看是否有参数，如果有，一定要在实例化时传
cai = Person(1,'男') #其实底层执行了__init__
cai.age = 20
print(cai.age)
print(cai.eye)
print(Person.eye)
print(cai.sex)

