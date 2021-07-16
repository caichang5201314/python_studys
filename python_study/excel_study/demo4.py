"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/14 16:28
@desciption: 读指定的一堆值
"""
from xlrd import open_workbook

bk = open_workbook(r'd:\mendao.xls') #bk是Book类的对象

sheet = bk.sheet_by_name('员工表') #sheet是Sheet类的对象

values = []
for i in range(7,sheet.nrows):
    values.append(sheet.row_values(i,4))
print(values)