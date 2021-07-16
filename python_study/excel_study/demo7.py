"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/15 10:55
@desciption: 写excel
会单独的生成新的excel表格

经验:
    1.当我查看代码中return陷入死局时,看注释中的return的解释或许能帮助我
"""
from xlwt import Workbook

wb = Workbook('utf-8') #wb是Workbook的对象
sheet = wb.add_sheet('部门表') #sheet是Worksheet的对象
sheet.write(1,4,'测试部')
wb.save(r'e:\部门表.xls')