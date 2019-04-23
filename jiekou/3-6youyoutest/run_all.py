# coding:utf-8
import unittest,os

def all_case():
    case_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'case') #获取当前目录下的case目录
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
    testcase.addTests(discover) # 直接加载 discover
    print(testcase)
    return testcase

if __name__ == "__main__":
    # 返回实例
    runner = unittest.TextTestRunner()
    # run 所有用例
    runner.run(all_case())