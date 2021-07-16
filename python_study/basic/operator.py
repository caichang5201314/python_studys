"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/12 10:45
@desciption:
运算符
    1.	赋值运算符:  =
    2.	算术运算符:  + ， - ， * ， / ， // ， % ， **
        1.	// 返回商的整数部分
        2.	% 返回余数    判断是否能被整除就要用它,读成'模' 20%3
        3.	**幂运算

        3.4都在if中运用
    3.	关系运算符:  >，<， ==， >=，<=，!=
    4.	逻辑运算符:  and，or，not
"""

name = 'caichang'

sal = 2000
comm = 100
total = sal + comm
print(total)

print(20 / 3)
print(20 // 3)

print(20 % 3)

print(20 ** 3)

if 20 > 3:
    print('ok')

if 20 > 3 and sal > 1500:
    print('good')

if 20 > 3 or sal > 15000:
    print('good2')

if 20 < 3 or sal > 15000:
    print('good3')

if not sal < 1500:
    print('good4')

number = int(input('请输入一个数:'))
# ==表示判断是否相等  =表示赋值
# 可千万别弄混淆了
if number % 3 == 0:
    print('能被3整除')
else:
    print('不能被3整除')
