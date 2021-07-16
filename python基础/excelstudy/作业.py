#1.把excel中的数据读出来插入到mysql表中
# from python基础.excelstudy.ExcelHelper import ExcelHelper
# from python基础.mysqlstudy.MySQLHelper import MySQLHelper
#
# excel = ExcelHelper()
# excel.book_path=r'd:\mendao_copy.xls'
# excel.sheet_name='员工表'
#
# data = excel.allvalues_by_row(7,21,5,7)
# print(data)
#
#
# mysql=MySQLHelper()
# mysql.host='localhost'
# mysql.password='root'
# mysql.database='blog'
#
# for i in range(len(data)):
#     sql = f"insert into student(name,sex) values ('{data[i][0]}',{data[i][1]})"
#     mysql.dml(sql)
#
# mysql.close()



#2.把mysql的数据读出来写入到excel中
from python基础.excelstudy.ExcelHelper import ExcelHelper
from python基础.mysqlstudy.MySQLHelper import MySQLHelper

mysql=MySQLHelper()
mysql.host='localhost'
mysql.password='root'
mysql.database='blog'

sql='select * from student where sex=0'
data = mysql.select(sql)
#print(data)

excel = ExcelHelper()
excel.add_sheet_name='学生信息'
excel.save_path=r'd:\学生信息表.xls'
title=['编号','姓名','性别']
excel.create_and_write(title,data)


