# -*-coding:utf-8-*
from HTMLTestRunner3.HTMLTestRunner import HTMLTestRunner
import unittest
import os
import time
'''获取当前case目录'''
case_dir = os.path.dirname(__file__)
'''报告路径'''
report_dir = os.path.dirname(os.path.dirname(__file__))
'''按路径加载用例'''
suite = unittest.defaultTestLoader.discover(case_dir)
'''获取当前时间戳并整理格式'''
now = time.strftime('%Y-%m-%d %H_%M_%S')
'''制作文件名字'''
report_name = report_dir +"/ReportHtml/"+now+"result.html"
'''报告写入'''
with open(report_name,"w") as f:
    runner = HTMLTestRunner(stream=f,title="goodstudy",description="daydayup")
    '''创建驱动并运行套件'''
    runner.run(suite)