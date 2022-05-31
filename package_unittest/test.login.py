
from work.diedai3 import  login
from loguru import login
"""
测试过程中，最小的单元就是测试用例(TestCase) . 在unittest做测试时，需要遵循如下规则：
所编写的测试用例，必须是一个类，而且必须继承TestCase类 。
1.每个测试方法，都是以test开头
2.编写测试类，建议以Test开头
3.编写的模块，建议小写test开头



"""


import unittest
class TestLogin(unittest.TestCase):
# 1.测试登录的测试用例
#case1:输入正确的用户和正确的密码进行登录
#case2:输入错误的用户名或密码登录
#case3：输入空的用户或密码登录



#2.进行测试— 使用断言：assert 值1 操作符 值2
#测试方法：预期结果和实际结果进行比较

#以上用例 登录成功的预期结果是code=0，


login_result = login('admin','123456')

logger.debug("登录返回数据：{}".format(login_result))
assert 0 = login_result.get('code')
assert 1 = login_result.get('code')

# 存在的问题 ：
"""
1. 无法查看运行的用例数，比如成功了几条，失败了几条
2. 如果失败了，是因为什么导致 ？ 最好给出失败的错误日志 。
3. 无法去组织用例 ，不能控制哪些用例执行，哪些不执行 ？