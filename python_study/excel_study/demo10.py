"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/15 16:26
@desciption: 往一个已存在的excel中写入数据
"""
from xlrd import open_workbook
from xlutils.copy import copy
from xlwt import XFStyle, Borders

wb = open_workbook(r'd:\mendao.xls', formatting_info=True)
new_wb = copy(wb)
new_sheet = new_wb.get_sheet(0)

borders = Borders()
borders.left = borders.THIN
borders.right = borders.THIN
borders.top = borders.THIN
borders.bottom = borders.THIN

style = XFStyle()
style.borders = borders

sheet = wb.sheet_by_name('员工表')  # sheet是Sheet类的对象
values = []
for i in range(7, sheet.nrows):
    values.append(sheet.row_values(i, 11, 13))
# print(values)

for j in range(len(values)):
    # print(values[j])
    if values[j][0] == values[j][1]:
        new_sheet.write(j + 7, 13, '通过', style)
    else:
        new_sheet.write(j + 7, 13, '不通过', style)

new_wb.save(r'd:\cc.xls')
