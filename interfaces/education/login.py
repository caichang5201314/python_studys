from requests import get
params={
    'account':'admin',
    'pwd':'660B8D2D5359FF6F94F8D3345698F88C'
}
cookies={
    'JSESSIONID':'49B629B0907F1B2E074B1C8986FEBC3C'
}
response = get('http://192.168.1.36:8080/recruit.students/login/in',params=params,cookies=cookies)
print(response.text)