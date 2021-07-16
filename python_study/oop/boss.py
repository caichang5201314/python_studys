"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/14 10:44
@desciption: 把昨天的函数变成类
"""


class HomeWork():

    def __init__(self):
        self.total = 0
        self.result = []
        self.month_day = 0

    def one(self):
        for i in range(1, 101):
            self.total = i + self.total
        print(f'他们的和为:{self.total}')

    def two(self):
        for i in range(1, 101):
            if i % 3 == 0 and i % 5 != 0:
                self.result.append(i)
        print(f'结果为:{self.result}')

    def three(self):
        for i in range(0, 51, 4):
            if i <= 50 - 15:
                self.total = self.total + 1
        print(f'{self.total}次能挑满')

    def four(self, date):
        year = int(date.split('-')[0])
        month = int(date.split('-')[1])
        day = int(date.split('-')[2])

        if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            total_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            total_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        for i in range(month - 1):
            self.month_day = total_list[i] + self.month_day
        self.total = self.month_day + day
        print(f'日期为今年的第{self.total}天')


hw = HomeWork()
# hw.one()
# hw.two()
# hw.three()
hw.four('2021-05-13')

