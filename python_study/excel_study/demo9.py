"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/15 11:13
@desciption: 写一堆值
content=[[10,'测试部','深圳'],[20,'开发部','重庆'],[30,'运维部','北京'],[40,'营销部','纽约']]
"""

from xlwt import Workbook, XFStyle, Font, Borders, Alignment, Pattern

wb = Workbook('utf-8')  # wb是Workbook的对象
sheet = wb.add_sheet('部门表')  # sheet是Worksheet的对象
title = ['部门编号', '部门名称', '部门位置']

font = Font()
font.bold = True
font.colour_index = 33

borders = Borders()
borders.left = borders.THIN
borders.right = borders.THIN
borders.top = borders.THIN
borders.bottom = borders.THIN

alignment = Alignment()
alignment.horz = alignment.HORZ_CENTER

# 颜色对照表:https://blog.csdn.net/zkw_1998/article/details/103930052
pattern = Pattern()
pattern.pattern = pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 7

style = XFStyle()
style.font = font
style.borders = borders
style.alignment = alignment
style.pattern = pattern

for i in range(len(title)):
    sheet.write(5, i + 4, title[i], style)  # 5-->第6行,i+4--->向右移动多少,+4,右移4

content = [[10, '测试部', '深圳'], [20, '开发部', '重庆'], [30, '运维部', '北京'], [40, '营销部', '纽约']]

content_style = XFStyle()
content_style.borders = borders

# j为行,k为列
for j in range(len(content)):
    for k in range(len(content[j])):
        sheet.write(6 + j, k + 4, content[j][k], content_style)

wb.save(r'e:\部门表.xls')
