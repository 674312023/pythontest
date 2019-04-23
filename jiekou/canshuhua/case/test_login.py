# coding:utf-8
import sys,os
#sys.path.append(r"D:\pythontest\jiekou\canshuhua")
sys.path.append('..')

import requests,unittest

from bolg.login import BlogLogin

class Test(unittest.TestCase):
    def setUp(self):
        s = requests.session()
        self.blog = BlogLogin(s)

    def test_login(self):
        result = self.blog.login()
        self.assertEqual(result['success'],True)



if __name__ == '__main__':
    unittest.main()
