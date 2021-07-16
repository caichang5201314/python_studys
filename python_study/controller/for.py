"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/13 9:42
@desciption: for
1.常规写法和变形写法
2.break和continue
  break:结束整个循环
  continue:结束本次循环
"""

#最常见写法
for i in range(10):
    print(i)

for i in ['caichang','caibao','hehe','haha']:
    print(i)

#只要in后是一个可迭代的对象(元组,列表,字符串)
emp = ['caichang','caibao','hehe','haha']
for i in emp:
    print(i)


print('hehe')
for i in range(1,11):
    if i%2==0:
        print(i)
        continue
    print('111')
print('haha')
