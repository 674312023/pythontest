# coding:utf-8
import unittest
import os
import HTMLTestRunner
#用例路径
case_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'case') #获取当前目录下的case目录

def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,pattern='test*.py',top_level_dir=None)
    print(discover)
    return discover

if __name__ == '__main__':
#    report_abspath = os.path.join(report_path, "result.html")
# 报告存放路径
    report_path = os.path.join(os.getcwd(), 'report')
    print(report_path)
    report_abspathname = os.path.join(report_path, 'result.html')
    print(report_abspathname)
#    fp = open(r''+ 'report_abspathname', 'wb+')
    fp = open(report_abspathname,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')

    # 调用add_case函数返回值
    runner.run(all_case())
    fp.close()
#    runner = unittest.TextTestRunner()
#    runner.run(all_case())
