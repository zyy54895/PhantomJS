from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
assert u"百度" in driver.title
elem = driver.find_element_by_name("wd")
elem.clear()
elem.send_keys(u"网络爬虫")
elem.send_keys(Keys.RETURN)
time.sleep(3)
assert u"网络爬虫." not in driver.page_source
# login_button = driver.find_element_by_xpath('//div[@id="u1"]/a[@name="tj_login"]')
# login_button.click()
# time.sleep(3)
# user_login = driver.find_element_by_xpath('//div[@class="tang-pass-footerBar"]/p[@title="用户名登录"]')
# user_login.click()
driver.close()

'''
代码分析：首先使用webdriver.Firefox()获取Firefox的驱动，调用get方法，打开百度首页，判断标题中是否包含百度字样，
接着通过元素名称wd获取输入框，通过send_keys方法将网络爬虫填写其中，然后回车。
延时3秒，判断搜索页面是否有网络爬虫字样，最后关闭driver。
'''
# from selenium.webdriver.common.by import By
# driver.find_element(By.XPATH, '//button[text()="some text"]')