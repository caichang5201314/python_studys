"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/13 14:27
@desciption: 参数
1.定参
  1.为什么要使用参数?
    当你写的业务中,发现数据有的有点'死'(不太灵活,需求变更后要自己手动该业务的数据)
    我不想自己该,而是做到客户你传什么,我就给你处理什么
  2.如何使用?
  3.默认值
    参数如果有默认值,传参时可以填(就按照填的执行),可以不填(不填按照默认值执行)
    注意:有默认值的参数要放在参数最后


2.变参(了解)
  工作后,你自己写代码可以不变参,但是要看得懂
"""


def one(start, end, step=1):
    total = 0
    for i in range(start, end, step):
        total = i + total
    print(f'他们的和为:{total}')


one(1, 101, 1)
one(5, 51, 5)
one(0, 200, 10)
one(1, 101)
