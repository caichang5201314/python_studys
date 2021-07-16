"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/12 11:18
@desciption: 浮点数

1.浮点变量=值
2.<class 'float'>
3.浮点除后依然为浮点,无论你能不能被整除(重点)
"""

score = 95.5
comm = 4000.0

print(type(score))

print(score / 5)
print(type(score / 5))

print(comm / 5)  # 浮点除后依然为浮点,无论你能不能被整除
