#conding:utf-8
from selenium import webdriver
import unittest
from time import sleep
import ddt
from youyou58 import excel
'''import sys
sys.path.append(r"D:\pythontest\selenium1\youyou58")
import excel'''
#testdata = ([{'username': 'python群', 'password': '123456'}, {'username': 'selenium群', 'password': '222222'}, {'username': 'appium群', 'password': '3333'}])
filepath = "D:\\pythontest\\selenium1\\youyou58\\testdata.xlsx"
sheetName = "Sheet1"
data = excel.ExcelUtil(filepath, sheetName).dict_data()
@ddt.ddt
class Blog(unittest.TestCase):
    u'登陆博客'
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        url = 'https://passport.cnblogs.com/user/signin'
        cls.driver.get(url)
        cls.driver.implicitly_wait(30)

    def login(self,username,psw):
        u'这里写了一个登录的方法,账号和密码参数化'
        self.driver.find_element_by_id('input1').clear()
        self.driver.find_element_by_id('input1').send_keys(username)
        self.driver.find_element_by_id('input2').clear()
        self.driver.find_element_by_id('input2').send_keys(psw)
        self.driver.find_element_by_id('signin').click()
        sleep(3)

    def is_login_sucess(self):
        u'''判断是否获取到登录账户名称'''
        try:
            text = self.driver.find_element_by_id("lnk_current_user").text
            print(text)
            return True
        except:
            return False

    @ddt.data(*data)
    def test_login(self,data):
        u'登陆案例参考'
        print("当前测试数据%s"%data)
        # 调用登录方法
        self.login(data["username"], data["password"])
        # 判断结果
        result = self.is_login_sucess()
        self.assertTrue(result)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

