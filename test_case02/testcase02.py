# -*-coding:utf-8-*-
import unittest
from Base.base_request import request
from Base.handle_value import getvmockvalue
from unittest import mock
host = "http://www.imooc.com/"
url = host+"api/updateversion"
class Test02(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_002(self):
        '''mock通过'''
        response = getvmockvalue.getvalue("getbanneradvertver2")
        request.run_main = mock.Mock(return_value=response)
        res  = request.run_main(url=url,method="get")
        self.assertEqual(res["id"],1)





