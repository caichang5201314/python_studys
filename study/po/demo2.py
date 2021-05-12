from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time




def open_browser():
    driver = webdriver.Chrome()
    return driver


def open_url(driver, url):
    driver.get(url)
    driver.maximize_window()


def login(driver, username, password):
    try:
        u_name = driver.find_element_by_name('username').send_keys(username)
        p_word = driver.find_element_by_name('password').send_keys(password)
        nlog_btn = driver.find_element_by_class_name('btn-a').click()
    except NoSuchElementException as msg:
        print(msg)


def check_login(driver):
    driver.switch_to.frame('main-frame')
    content = driver.find_element_by_xpath('/html/body/h1/span[1]/a').text
    print(content)
    if content == 'ECSHOP 管理中心':
        print('登录成功')
    else:
        raise NameError('user name error!')
    # driver.find_element_by_link_text('退出').click()
    # time.sleep(1)


def close(driver):
    driver.quit()

if __name__ == '__main__':
    """
    ECShop登录
    """
    url = ' http://localhost/ecshop/admin'
    username = 'caichang'
    password = 'caichang1'
    driver = open_browser()
    open_url(driver,url)
    login(driver,username,password)
    check_login(driver)
    close(driver)