"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/13 10:28
@desciption: 1+2+3+....+100的和
"""

total=0
for i in range(1,101):
    total=i+total
print(f'他们的和为:{total}')