"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/14 16:28
@desciption: 读一个单元格
"""
from xlrd import open_workbook

bk = open_workbook(r'd:\mendao.xls') #bk是Book类的对象
sheet = bk.sheet_by_name('员工表') #sheet是Sheet类的对象
cell_value = sheet.cell_value(14,5)
print(cell_value)
