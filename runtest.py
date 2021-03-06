# coding=utf-8

import time
import unittest
import HTMLTestRunner
from common.SendEmail import Email

email = Email()
all_case = 'E:\\App-Test\\testcase'
# all_case = '/Users/xintudoutest/github/Appium/testcase'


def create_suite():

    """
        使用discover查找出testcase文件夹下的所有test开头的.py文件
    """
    test_suite = unittest.TestSuite()  # 创建测试套件
    discover = unittest.defaultTestLoader.discover(all_case,
    pattern ='test_*.py', top_level_dir=None)

    """
        使用for循环出suite,再循环出case
    """
    for suite in discover:
        for case in suite:
            test_suite.addTests(case)
            print(test_suite)
    return test_suite


def run_test():
    """
        运行测试用例，生成测试报告
    """
    test_case = create_suite()
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filename = 'E:\\App-Test\\report\\' + now + "Myreport.html"
    # filename = '/Users/xintudoutest/github/Appium/report/' + now + "Myreport.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'测试用例结果', tester=u'宇宙超级无敌大圈圈')
    runner.run(test_case)
    fp.close()


if __name__ == "__main__":
    run_test()
    email.send_mail()

