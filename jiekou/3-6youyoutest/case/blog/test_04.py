# coding:utf-8
import unittest
from time import sleep

class Test(unittest.TestCase):

    def setUp(self):
        print('start')

    def tearDown(self):
        sleep(1)
        print('end')

    def test04(self):
        print('执行测试用例04')


if __name__ == '__main__':
    unittest.main()