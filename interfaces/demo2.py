from json import loads
from urllib.request import Request

from requests import get

params = {
    'phone': 18602355173,
    'key': 'b07c85237609fc6005e5ef8f81a7f2fc',
    'dtype': 'json'
}

response = get('http://apis.juhe.cn/mobile/get', params=params)
print(response.text)
print(type(response.text))

response_text = loads(response.text)
if response_text['error_code'] == 0:
    print('测试通过')
else:
    print('测试失败')
