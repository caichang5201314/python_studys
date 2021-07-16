"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/13 14:03
@desciption: 函数定义和调用
定义: def===>define
def 函数名():
    业务

调用:
函数名()
"""

#定义
def one():
    total = 0
    for i in range(1, 101):
        total = i + total
    print(f'他们的和为:{total}')


def two():
    result = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 != 0:
            result.append(i)
    print(f'结果为:{result}')


def three():
    count = 0
    for i in range(0, 51, 4):
        if i <= 50 - 15:
            count = count + 1
    print(f'{count}次能挑满')


def four():
    date = input('请输入日期,如:2021-05-13:')
    year = int(date.split('-')[0])
    month = int(date.split('-')[1])
    day = int(date.split('-')[2])
    total = 0

    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        total_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        total_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    month_day = 0
    for i in range(month - 1):
        month_day = total_list[i] + month_day
    total = month_day + day
    print(f'日期为今年的第{total}天')

#调用
#one()