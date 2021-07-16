"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/13 15:54
@desciption: 变参(了解)
定义时， *将参数配成元组；调用时，*将元组或列表打散成参数进行参数传递
定义时，**将参数装配成字典；调用时，**将字典打散成参数进行参数传递
"""


def register(username, password, *args):
    print(username, password, args)


register(111, 222)
register(111, 222, 213, 213, 213, 123, 213, 1232, 13)
register(111, 222, 213, 213)


def register2(username, password, **kwargs):
    print(username, password, kwargs)


register2(111, 222)
register2(111, 222, a=213, b=2131)
register2(111, 222, a=213, b=2131, c='dadsd', d='dasdsad')


def one(*args):
    total = 0
    for i in range(args[0], args[1], args[2]):
        total = i + total
    return total


c = one(1, 101, 1)
print(c)


# 有参有返回
def four(**kwargs):
    total = 0
    for i in range(kwargs['start'], kwargs['end'], kwargs['step']):
        total = i + total
    return total


c = four(start=1, end=101, step=1)
print(c)

print(abs(-5))
print(min(12,321,321,312,312,321,312,321,312,321,2))