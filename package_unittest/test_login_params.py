
#问题：测试用例过多，导致代码冗余

# 具体方法 ： expand(list) ,list : 数据列表
# 备注 ：使用了expand()，需要把它放在测试方法前，加@ ，这个叫装饰器(下去了解)

# 前置条件 ： 下载安装：pip install parameterized


# 1. 导入包
from parameterized import parameterized
import unittest

from work.diedai3 import login

lst_data = [(0,'admin','123456'),(0,'dev','123456'),(1,'dev','1234567'),(1,'hahha',' ')]

class TestLogin(unittest.TestCase):#装饰器


    @parameterized.expand(lst_data)
    def test_login(self,except_value,username,password):

        actual_value = login(username,password).get('code') #此处login需要导入数据;alt+enter
        self.assertEqual(except_value,actual_value)


if __name__ == '__main__':
    unittest.main()