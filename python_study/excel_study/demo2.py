"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/14 16:27
@desciption: 读一列
"""
from xlrd import open_workbook

bk = open_workbook(r'd:\mendao.xls') #bk是Book类的对象
sheet = bk.sheet_by_name('员工表') #sheet是Sheet类的对象
col_values = sheet.col_values(5,7)
print(col_values)
