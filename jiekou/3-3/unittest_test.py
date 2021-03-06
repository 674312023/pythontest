# coding:utf-8
import unittest

class Test(unittest.TestCase):
    def test01(self):
        print('1')
        '''判断a==b'''
        a = 1
        b = 1
        self.assertEqual(a, b)

    def test02(self):
        print('2')
        '''判断a in b'''
        a = 'hello'
        b = 'hello world'
        self.assertIn(a, b, msg='a不在 %s里面 != %s' % (a, b))

    def test03(self):
        print('3')
        '''判断a为True'''
        a = True
        self.assertTrue(a)

    def test04(self):
        '''失败用例'''
        print('4')
        a = '帅哥'
        b = '不是帅哥'
        self.assertEqual(a, b,msg='两个数不相等%s !=%s' % (a, b) )
    def test(self):
        '''失败用例'''
        print('5')
        a = '帅哥'
        b = '不是帅哥'
        self.assertEqual(a, b,msg='两个数不相等%s !=%s' % (a, b) )
if __name__ == '__main__':
    unittest.main()