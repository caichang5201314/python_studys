from json import loads

from requests import post

url = 'http://192.168.1.36:8080/recruit.students/school/manage/setStudentRecruitTime'
json = [{"id": "5794", "recruitStartTime": "2021-06-02", "recruitEndTime": "2021-06-05", "isStudentRecruitTime": "1"}]
cookies = {
    'JSESSIONID': '49B629B0907F1B2E074B1C8986FEBC3C'
}
response = post(url=url, json=json, cookies=cookies)
print(response.text)
response_text = loads(response.text)
if response_text['data'][0]['id'] == int(json[0]['id']):
    print('测试通过')
else:
    print('测试失败')
