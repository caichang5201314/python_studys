from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
element = driver.find_element_by_id('kw')
print(element.get_attribute('outerHTML'))
