"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/12 15:25
@desciption: 列表
1.它创建,访问,遍历和元素一模一样,只是把()变成[]
2.列表是数据结构中的链表,因此他有自己独有的方法,而我们学习的重点是掌握这些独有方法
3.元组和列表的区别? (自查,笔试不考,面试少考)
4.我自己用,几乎全部是列表,元组这辈子就用不上
"""
emp = []
emp = [7369, 'SMITH', 'CLERK', 7902, '1980-12-17', 800.00, None, 10, True]  # 一维
emp = [[1, '张飞'], [2, '刘备'], [3, '关羽']]  # 二维

emp = [7369, 'SMITH', 'CLERK', 7902, '1980-12-17', 800.00, None, 10, True]  # 一维
print(emp[2])  # 常用
print(emp[-7])
print(emp[0:4])

for i in range(len(emp)):
    print(emp[i])


#m===method
emp = [7369, 'SMITH', 'CLERK', 7902, '1980-12-17', 800.00, None, 10, True]

#添加
emp.append('凤姐')
print(emp)
emp.insert(2,(11,22,33))
print(emp)

#删除
emp.pop(2)
print(emp)
emp.pop()
print(emp)
emp.remove('SMITH')
print(emp)

#排序
emp=[12,321,32,1321,321,343,5,35,4132,45435,2,4]
emp.sort()
print(emp)
emp.reverse()
print(emp)

