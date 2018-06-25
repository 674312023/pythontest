# coding:utf-8
import unittest,requests


class KuaidiTest(unittest.TestCase):
    def setUp(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        self.s = requests.session()

    def test_yunda(self):
        danhao = '1202247993797'
        kd = 'yunda'
        self.url = 'http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html' % (danhao, kd)
        print(self.url)
        # 第一步发请求
        r = self.s.get(self.url, headers=self.headers, verify=False)
        print(r.status_code)
        result = r.json()
        # 第二步获取结果
        print(result['company'])  # 获取公司名称
        data = result["data"] # 获取 data 里面内容
        print(data[0]) # 获取 data 里最上面有个
        get_result = data[0]['context'] # 获取已签收状态
        # 断言：测试结果与期望结果对比
        self.assertEqual(result['company'], '韵达快递')
        self.assertIn('已签收', get_result)
    def test_tiantian(self):
        danhao = ''

if __name__ == '__main__':
    unittest.main()



