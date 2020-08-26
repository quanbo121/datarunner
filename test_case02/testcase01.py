# -*-coding:utf-8-*-
import unittest
'''导入实例化后的对象'''
from Base.base_request import request
url="http://www.imooc.com/api/updateversion"
class Test01(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_001(self):
        '''调用封装的方法验证updatversion接口参数为空'''
        res=request.run_main(method="get",url=url)

        self.assertEqual(1001,res["errorcode"])

