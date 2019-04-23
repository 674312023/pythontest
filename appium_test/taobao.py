# coding:utf-8

from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

des = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:7555',
    'platformVersion': '6.0.1',
    'appPackage': 'com.taobao.taobao',
    # apk 的 launcherActivity
    'appActivity': 'com.taobao.tao.welcome.Welcome'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
sleep(10)
#driver.find_element_by_id('com.taobao.taobao:id/yes').click()

def always_allow(driver, number=5):
    '''
    fuction:权限弹窗-始终允许
    args:1.传driver
    2.number，判断弹窗次数，默认给5次
    其它： 
    WebDriverWait里面0.5s判断一次是否有弹窗，1s超时
    '''
    for i in range(number):
        loc = ("xpath", "//*[@text='允许']")
        loc1 = ("xpath", "//*[@text='同意']")
        try:
            e = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located(loc))
            e.click()
        except:
            pass
        try:
            e = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located(loc1))
            e.click()
        except:
            pass


if __name__ == '__main__':
    always_allow(driver)
    sleep(5)
    driver.find_element_by_id("com.taobao.taobao:id/home_searchedit").click()
    driver.find_element_by_id("com.taobao.taobao:id/searchEdit").click()
    sleep(1)
    driver.find_element_by_id("com.taobao.taobao:id/searchEdit").send_keys(u"python")
    driver.find_element_by_id('com.taobao.taobao:id/searchbtn').click()
