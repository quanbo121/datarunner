# -*-coding:utf-8-*-
import ddt
import unittest
from HTMLTestRunner3.HTMLTestRunner import HTMLTestRunner
import time
from Base.base_request import *
from Base.handle_result import *
from Base.handle_cookie import *
from Base.handle_header import *
from Base.codition_data import *
'''去掉之前框架中的data，现在的data给它重新赋值'''
data = excel_data.get_excel_data()

'''利用ddt，进行数据驱动'''
@ddt.ddt
class TestRunCserDdt(unittest.TestCase):
    def setUp(self):
        print("case开始执行")

    def tearDown(self):
        print("执行结束")

    @ddt.data(*data)
    def test_main_case(self,data):
        '''给一个默认值'''
        cookies = None
        get_cookie = None
        headers = None
        '''i就是行号'''
        i = excel_data.get_rows_number(data[0])
        is_run = data[2]
        '''判断如果第二列数据为yes则执行'''
        if is_run == "yes":
            try:
                '''获取前置条件'''
                is_depend = data[3]
                '''如果前置条件存在，获取依赖字段'''
                data1 = json.loads(data[7])
                if is_depend:
                    depend_key = data[4]
                    depend_data = get_data(is_depend)
                    data1[depend_key] = depend_data
                '''获取请求方法'''
                method = data[6]
                '''获取请求url'''
                url = data[5]
                cookie_method = data[9]
                header_method = data[8]
                if cookie_method == "yes":
                    cookies = handlecookie.get_cookie_value("app")
                if cookie_method == "write":
                    get_cookie = {"is_cookie": "web"}
                    '''操作header的情况'''
                if header_method == "yes":
                    headers = getHeader.get_header()
                '''用封装的request发送请求'''
                res = request.run_main(method=method, url=url, get_cookie=get_cookie, cookies=cookies, headers=headers,
                                       data=data1)
                excel_data.excel_write_data(i,14,json.dumps(res))
                '''获取实际errorCode对应的code'''
                code = res["errorCode"]
                '''获取实际的msg的值'''
                msg = res["errorDesc"]
                '''获取断言方法'''
                assertion_method = data[10]
                '''获取预期结果'''
                excepect_result = data[11]

                '''如果断言方法是mer'''
                if assertion_method == "mer":
                    '''传入实际code获取config对应的msg值'''
                    config_msg = data_result.get_result(url, code)
                    '''进行断言'''
                    try:
                        self.assertEqual(msg,config_msg)
                        excel_data.excel_write_data(i, 13, "case通过")
                    except Exception as e:
                        excel_data.excel_write_data(i, 13, "case失败")
                        raise e

                '''如果断言方法是result'''
                if assertion_method == "result":
                    try:
                        self.assertEqual(str(res["errorCode"]),excepect_result)
                        excel_data.excel_write_data(i, 13, "case通过")
                    except Exception as e:
                        excel_data.excel_write_data(i, 13, "case失败")
                        raise e


            except Exception as e:
                excel_data.excel_write_data(i, 13, "case失败")

if __name__ == '__main__':
    # '''获取当前case目录'''
    # case_dir = os.path.dirname(__file__)
    # '''报告路径'''
    # report_dir = os.path.dirname(os.path.dirname(__file__))
    # '''按路径加载用例'''
    # suite = unittest.defaultTestLoader.discover(case_dir)
    # '''获取当前时间戳并整理格式'''
    # now = time.strftime('%Y-%m-%d %H_%M_%S')
    # '''制作文件名字'''
    # report_name = report_dir + "/ReportHtml/" + now + "result.html"
    # '''报告写入'''
    # print(report_name)
    # with open(report_name, "w") as f:
    #     runner = HTMLTestRunner(stream=f, title="goodstudy", description="daydayup")
    #     '''创建驱动并运行套件'''
    #     runner.run(suite)
    unittest.TextTestRunner(verbosity=2)