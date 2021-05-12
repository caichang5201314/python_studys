from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
element = driver.find_element_by_partial_link_text('地')
print(element.get_attribute('outerHTML'))
