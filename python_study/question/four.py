"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/13 11:23
@desciption: 输入一个日期,如:2021-05-13,判断今天是整年的多少天
天数:31+28+31+30+13
提示:闰年判断:
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
"""
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
