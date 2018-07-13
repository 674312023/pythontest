#coding:utf-8
from selenium import webdriver
from time import sleep
url='file:///C:/Users/shen/Desktop/test/selenium/youyou28table/table.html'
driver=webdriver.Firefox()
driver.get(url)
sleep(4)
t=driver.find_element_by_xpath(".//*[@id='myTable']/tbody/tr[2]/td[1]")
print(t.text)
driver.quit()
