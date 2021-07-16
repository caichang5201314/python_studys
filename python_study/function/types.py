"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/13 15:06
@desciption: 函数的4种表现形式
面对任何一个功能,都可以写成4种表现形式,至于你采用哪种来表现你的功能,由具体业务来决定

写的经验:
1.我写代码时,首先也业务
2.封装成一个无参无返回的函数
3.审视一下我的代码,看看有没有可以变得灵活的地方,如果有,把这些'死'变成参数传
4.再审视一下我的代码,看看是不是要把这个函数的值抛出去而不是我直接处理,如果是,改成return结构

"""
#无参无返回
def one():
    total = 0
    for i in range(1, 101):
        total = i + total
    print(f'他们的和为:{total}')

#有参无返回
def two(start,end):
    total = 0
    for i in range(start,end):
        total = i + total
    print(f'他们的和为:{total}')

#无参有返回
def three():
    total = 0
    for i in range(1, 101):
        total = i + total
    return total

#有参有返回
def four(start,end):
    total = 0
    for i in range(start,end):
        total = i + total
    return total
