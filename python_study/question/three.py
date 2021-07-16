"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/13 11:05
@desciption: 挑水
水缸:50L
已有:15L,每次挑4L
问:几次能挑满
"""

count =0

for i in range(0,51,4):
    if i<=50-15:
        count=count+1

print(f'{count}次能挑满')



