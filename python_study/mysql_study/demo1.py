"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/16 9:09
@desciption: 查询数据
"""
from pymysql import connect

conn = connect('192.168.1.13','root','root','caichang',3306) # conn是Connection类的对象
cursor = conn.cursor() # cursor 是Cursor类的对象

cursor.execute('select * from dept')
#fetchall()--> 查出所有,二维
#fetchone()--> 查出一条,一维
#fetchmany(个数)-> 查出给定的条数,二维
result = cursor.fetchall()
print(result)

cursor.close() # 关闭游标
conn.close()   #关闭链接

