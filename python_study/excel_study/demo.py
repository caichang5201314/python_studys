"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/14 15:58
@desciption:
1.如果是个函数,首先看是否有返回值,如果有,马上用一个对象去接收这个返回
2.然后看是否有必填参数,如果有,依次传入参数
3.接收后的变量到底是什么,要慢慢的跟踪代码才知道(一般是类或函数或其他类型,都有可能)
4.如果是个类,那么你这个变量就是'对象'
5.那你接下来的一切行为都是对象.
  但是能.出什么来,就要跟'结构树'才能看到
      结构树打开方式:alt+7,建议挪到右侧
6.请耐心的慢慢去品味结构树中体现的方法和属性等(心急没用,甚至你要慢慢做实验在知道是不是你要的)
  没有什么帮助手册给你.一切靠自己
"""
from xlrd import open_workbook

# 打开工作簿
bk = open_workbook(r'd:\mendao.xls') #bk是Book类的对象

# 打开对应的Sheet
sheet = bk.sheet_by_name('员工表') #sheet是Sheet类的对象

row_values = sheet.row_values(8,4)
print(row_values)



