# -*-coding:utf-8-*-
import unittest
import os
import sys
'''获取工程目录'''
path_now = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
'''把工程目录加到环境变量里，可以解决找不到模块的问题'''
sys.path.append(path_now)
'''导入用例'''
from test_case02.testcase01 import Test01
from test_case02.testcase02 import Test02
from test_case02.testcase03 import Test03
'''加载用例'''
case01 = unittest.TestLoader().loadTestsFromTestCase(Test01)
case02 = unittest.TestLoader().loadTestsFromTestCase(Test02)
case03 = unittest.TestLoader().loadTestsFromTestCase(Test03)
'''把加载的用例放到容器里'''
waitrun = unittest.TestSuite([case01,case02,case03])
'''创建驱动并运行套件'''
unittest.TextTestRunner(verbosity=2).run(waitrun)
