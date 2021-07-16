"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/13 10:50
@desciption: 100以内,能被3整除,不能被5整除的数,结果形成一个列表
"""

result=[]
for i in range(1,101):
    if i%3==0 and i%5!=0:
        result.append(i)
print(f'结果为:{result}')