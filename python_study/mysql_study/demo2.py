"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/16 10:05
@desciption: 增删改
"""
from pymysql import connect

conn = connect('192.168.1.13','root','root','caichang',3306) # conn是Connection类的对象
cursor = conn.cursor() # cursor 是Cursor类的对象

cursor.execute("delete from dept where deptno=50")


cursor.close() # 关闭游标
conn.close()   #关闭链接
