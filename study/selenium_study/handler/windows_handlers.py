from selenium import webdriver

import time

""" 
多窗口切换 
"""

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
# 获得当前窗口
sreach_windows = driver.current_window_handle
print(sreach_windows)
driver.find_element_by_link_text('登录').click()
driver.implicitly_wait(5)
driver.find_element_by_link_text('立即注册').click()

# 获取所有窗口句柄
all_handles = driver.window_handles
print(all_handles)
# # 进入注册窗口页面
for handle in all_handles:
    if handle != sreach_windows:
        # 切换窗口
        driver.switch_to.window(handle)
        driver.find_element_by_name("userName").send_keys("userName")
time.sleep(2)
#
# 进入搜索窗口页面
for handle in all_handles:
    if handle == sreach_windows:
        # 切换窗口
        driver.switch_to.window(handle)
        #driver.back()
time.sleep(5)
driver.find_element_by_id("kw").send_keys("Selenium")
#driver.find_element_by_id("su").click()
time.sleep(2)
driver.quit()
