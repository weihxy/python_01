


#问题：用unittest的测试报告太简单，想生成更为详细的测试报告

#解决方案：使用HMTLTestRunnner模块生成测试报告，可以使用浏览器打开

# 前置条件：直接现成



from work.diedai3 import login
import unittest
import sys

from package_unittest.HTMLTestRunner import HTMLTestRunner

class TestLogin(unittest.TestCase):



    # 1. 测试登录的测试用例

    # case1 : 输入正确的用户和正确的密码进行登录
    def test_login_success(self):
        print("开始运行方法：", sys._getframe().f_code.co_name)
        except_value = 0
        actual_value = login('admin','123456').get('code')
        self.assertEqual(except_value,actual_value)

    # case2 : 输入错误的用户名或密码登录
    def test_user_wrong(self):
        print("开始运行方法：", sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login('bca', '123456').get('code')
        self.assertEqual(except_value, actual_value)

    # case3 : 输入空的用户或密码登录
    def test_password_is_null(self):
        print("开始运行方法：", sys._getframe().f_code.co_name)
        except_value = 2
        actual_value = login('admin', '').get('code')
        self.assertEqual(except_value, actual_value)


"""
b. TestSuite()功能：
  1.可以添加不同的测试用例到套件中
  2.可以添加不同的测试用例组到陶建忠

c.TextTestRunner()功能：
  1.可以将测试套件进行运行
"""
if __name__ == '__main__':
    suite_a = unittest.TestSuite()
    suite_a.addTest(TestLogin('test_login_success'))
    suite_a.addTest(TestLogin('test_user_wrong'))
    suite_a.addTest(TestLogin('test_password_is_null'))

    print(suite_a)

#创建一个测试报告文件，是HTML格式的
    test_report = './test_report.html'
    with open(test_report,'wb') as f:
        runner = HTMLTestRunner(f,title = '测试报告',description='测试报告描述')
        runner.run(suite_a)
