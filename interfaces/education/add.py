from json import loads

from requests import post

url = 'http://192.168.1.36:8080/recruit.students/school/manage/addSchoolInfo'
data = {
    'schoolName': '凤姐你好2',
    'remark': '凤姐很好2',
    'listSchoolType[0].id': 2,
    'canRecruit': 1
}
cookies={
    'JSESSIONID':'49B629B0907F1B2E074B1C8986FEBC3C'
}
response = post(url=url, data=data,cookies=cookies)
print(response.text)
response_text = loads(response.text)
if response_text['message'] != '该学校已存在，不能重复新建。':
    print('测试通过')
else:
    print('测试失败')