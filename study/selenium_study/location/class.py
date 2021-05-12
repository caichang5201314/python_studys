from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
element = driver.find_element_by_class_name('s_ipt')
print(element.get_attribute('outerHTML'))
