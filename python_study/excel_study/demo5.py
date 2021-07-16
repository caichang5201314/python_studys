"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/14 16:29
@desciption: 把业务封装成函数
1.养成一个相同东西写一次的习惯
2.参数和返回值的灵活运用
"""
from xlrd import open_workbook


def get_sheet():
    bk = open_workbook(r'd:\mendao.xls')  # bk是Book类的对象
    sheet = bk.sheet_by_name('员工表')  # sheet是Sheet类的对象
    return sheet


def get_value_by_row():
    row_values = get_sheet().row_values(8, 4)
    return row_values


def get_value_by_col():
    col_values = get_sheet().col_values(5, 7)
    return col_values


def get_value_by_cell():
    cell_value = get_sheet().cell_value(14, 5)
    return cell_value


def get_all():
    values = []
    for i in range(7, get_sheet().nrows):
        values.append(get_sheet().row_values(i, 4))
    return values


# print(get_value_by_row())
# get_value_by_col()
# get_value_by_cell()
# get_all()
