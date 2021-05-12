from selenium import webdriver

mobileEmulation = {"deviceName":"iPhone 6"}
options = webdriver.ChromeOptions()
options.add_experimental_option("mobileEmulation", mobileEmulation)
driver = webdriver.Chrome(options=options)
driver.get("http://www.baidu.com")
driver.find_element_by_name('word').send_keys('caichang')
driver.find_element_by_id('index-bn').click()

