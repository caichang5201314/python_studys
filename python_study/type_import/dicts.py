"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/12 16:15
@desciption: 字典 dict
1.创建
2.访问
3.我们以后的接口测试中的返回值是json格式,这个json和字典转化一下就就可以,所以字典非常重要
"""

emp = {
    "empno": 7788,
    "ename": 'caichang',
    "family": ('cai10', 'caidm', 'fbs', 'caij'),
    "comm": 300.00,
    "sal": 200000,
    "girlfriend": None,
    "is_sz_person": False
}
print(type(emp))
print(emp['family'][3])

# 访问
print(emp['ename'])

data = {
    "resultcode": "200",
    "reason": "Return Successd!",
    "result": {
        "province": "重庆",
        "city": "",
        "areacode": "023",
        "zip": "404100",
        "company": "联通",
        "card": ""
    },
    "error_code": 0
}

print(data['result']['company'])

print(data.keys())
print(data.values())


print(list(data.keys())[-1])

print(data.get('result').get('company')) # 忘记它

