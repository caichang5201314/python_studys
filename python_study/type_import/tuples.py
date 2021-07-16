"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/12 14:01
@desciption: 元组 tuple
1.创建
2.访问
3.遍历
    一维:插入,更新,全删/部分删
    二维:查询,列表
"""

# 创建
emp = ()
emp = (7369, 'SMITH', 'CLERK', 7902, '1980-12-17', 800.00, None, 10, True)  # 一维
emp = ((1, '张飞'), (2, '刘备'), (3, '关羽'))  # 二维

# 访问
#       0       1        2      3         4          5       6    7    8
emp = (7369, 'SMITH', 'CLERK', 7902, '1980-12-17', 800.00, None, 10, True)
#       -9     -8       -7     -6        -5         -4      -3   -2    -1
# 访问方式通过下标访问
print(emp[2])  # 常用
print(emp[-7])

# 切片
print(emp[0:4])  # 从0开始,取到4但不包含4  [0,4)  常见
print(emp[0:-5])
print(emp[-9:-5])
print(emp[:4])
print(emp[5:])
# 不能这样
print(emp[5:2])  # 第一个值确定后,后面第二个值只能是第一个值的右边位,否则数据为空


#二维访问
#           0           1           2
emp = ((1, '张飞'), (2, '刘备'), (3, '关羽'))

print(emp[0])
print(emp[0][1])


#遍历


emp = (7369, 'SMITH', 'CLERK', 7902, '1980-12-17', 800.00, None, 10, True)
# print(emp[0])
# print(emp[1])
# print(emp[2])
# print(emp[3])

# 一维的遍历
for i in range(len(emp)):
    print(emp[i])


emp = ((1, '张飞','屠夫'), (2, '刘备'), (3, '关羽'),(4,'曹操','校尉'))
#        00   01     10   11     20   21
# 二维遍历
# i==外层  j==内层
print(len(emp))
for i in range(len(emp)):
    for j in range(len(emp[i])):
        print(emp[i][j])


# emp = select * from emp where id=123  一维
#value=emp[1]  value=emp[3]


# insert into emp(ename,job) values (emp[0],emp[1])

