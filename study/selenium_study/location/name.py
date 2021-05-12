from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
element = driver.find_element_by_name('wd')
print(element.get_attribute('outerHTML'))
