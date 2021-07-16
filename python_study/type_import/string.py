"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/12 17:07
@desciption: 字符串  str
1.单引号和双引号都可以
2.r和f的灵活运用
  r:凡这个字符串中有我们要转义的字符,前面直接加r即可
    以后我只要是字符串,前面带个r,小心无大错
  f:新特性,用起来简单,过程很烦  字符串的格式化
3.可以把字符串当元组看  工作很少用
4.他有自己独有的方法(超级重点)
"""

name='caichang'
name="caichang"

#msg = 'i'm ok'
msg = "i'm ok"
print(msg)
msg = 'i\'m ok' #转义符
print(msg)

url=r'http://www.baidu.com?id=5&page=3'
path=r'd:\naichang\c\d.txt'
print(path)


name='蔡昶'
age=35
address='贵州遵义'
marry='单身'

print('我叫name,今年age,来自贵州address,marry')

#C语言写法
print('我叫%s,今年%d,来自贵州%s,%s' %(name,age,address,marry))

#java写法
print('我叫'+name+',今年'+str(age)+',来自贵州'+address+','+marry)

#新特性 f
print(f'我叫{name},今年{age},来自贵州{address},{marry}')


name="caichang is a good teacher"
print(name[1])
for i in range(len(name)):
    print(name[i])

name="caichang is a good teacher"
print(name.upper())
print(name.capitalize())
print(name.title())
print(name.split(' '))
print(name.split(' ')[3])
