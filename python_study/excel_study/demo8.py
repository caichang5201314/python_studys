"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/15 11:11
@desciption: 写一行
title =['部门编号','部门名称','部门位置']
"""

from xlwt import Workbook

wb = Workbook('utf-8') #wb是Workbook的对象
sheet = wb.add_sheet('部门表') #sheet是Worksheet的对象
title =['部门编号','部门名称','部门位置']
for i in range(len(title)):
    sheet.write(5,i+4,title[i]) #5-->第6行,i+4--->向右移动多少,+4,右移4
wb.save(r'e:\部门表.xls')
