"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/13 14:56
@desciption: 返回值
1.什么时候用return?
  这个函数仅仅提供数据供调用者处理,他本身不处理

2.如何调有return的函数?
  1.用一个参数去接收这个函数
  2.拿到这个函数的返回值后,你可以随意的开展你的业务代码的编写


"""


# 南航抛出定机票的方法
def one(start, end, step=1):
    total = 0
    for i in range(start, end, step):
        total = i + total
    return total


# 我自己写的项目
a = one(1, 101)
print(a)

# 美团
a = one(1, 101)
if a > 5000:
    print('ok')

# 携程
c = one(1, 101)
print(f'机票价格为:{c + 50}')
