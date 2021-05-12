from selenium import webdriver

options = webdriver.IeOptions()
options.add_argument("--headless")  # 隐藏浏览器
driver = webdriver.Ie(options=options)   # 打开谷歌浏览器
driver.get("http://www.baidu.com/")  # 输入百度网址
print(driver.title)  # 获取百度标题
driver.quit()  # 关闭浏览器
