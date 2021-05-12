from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
a = driver.find_elements_by_tag_name('a')
# 打印标签名为a的个数
print(len(a))
for e in a:
    if e.get_attribute("name") == "tj_briicon":
    # 打印标签名为a，name属性值为tj_trmap的文本信息
        print(e.text)# 打印元素的text文本