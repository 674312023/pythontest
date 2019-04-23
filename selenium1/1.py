# coding:utf-8
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')  # 静默模式
# 打开chrome浏览器
driver = webdriver.Chrome(chrome_options=options)
# driver = webdriver.Chrome()

driver.get("https://www.cnblogs.com/yoyoketang")
print(driver.title)