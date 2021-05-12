from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

""" 
ECShop登录 
"""
url = ' http://localhost/ecshop/admin'
user_name = 'caichang'
pass_word = 'caichang1'


def login_test():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()

    try:
        u_name = driver.find_element_by_name('username')
        p_word = driver.find_element_by_name('password')
        nlog_btn = driver.find_element_by_class_name('btn-a')
    except NoSuchElementException as msg:
        print(msg)

    u_name.clear()
    u_name.send_keys(user_name)
    time.sleep(1)
    p_word.clear()
    p_word.send_keys(pass_word)
    time.sleep(1)
    nlog_btn.click()
    time.sleep(1)
    driver.switch_to.frame('main-frame')
    content = driver.find_element_by_xpath('/html/body/h1/span[1]/a').text
    print(content)
    if content == 'ECSHOP 管理中心':
        print('登录成功')
    else:
        raise NameError('user name error!')
    #driver.find_element_by_link_text('退出').click()
    #time.sleep(1)
    driver.quit()

if __name__ == '__main__':
    login_test()
