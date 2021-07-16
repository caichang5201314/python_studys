from requests import get, Response

response = get('http://www.baidu.com')
print(response.text)