"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/13 9:04
@desciption: if  注意缩进,IDE工具会自动完成缩进行为

1.if....else....
2.只有单if
3.if并行 查询时
4.if...elif....elif....else.....
5.if嵌套
"""

# name = input('请输入你的名字:')
# if name=='admin':
#     print('登录成功')
# else:
#     print('登录失败')

# login_name = input('你的登录账号为:')
# if login_name!='admin':
#     print('没有权限')
# print('其他的业务代码')


# age=int(input('你的年龄:'))
# if age>=35:
#     print('对不起,太老了,不符合最大当兵年龄')
# elif age>=18:
#     print('可以当兵')
# elif age>=16:
#     print('当预备兵')
# else:
#     print('长几年再来')

#登录 admin/admin 1234

username = input('请输入你的用户名:')
password = input('请输入你的密码:')
verify = int(input('请输入验证码:'))


if verify==1234:
    if username=='admin':
        if password=='admin':
            print('登录成功')
        else:
            print('密码错误')
    else:
        print('用户名不存在')
else:
    print('验证码不正确')


