# -*-coding:utf-8-*-

from Base.base_request import *
from Base.handle_result import *
from Base.handle_cookie import *
from Base.handle_header import *
from Base.codition_data import *
'''创建RunMain类实现运行用例的功能'''
class RunMain:

    def run_case(self):

        ''' 获取行数'''
        rows = excel_data.get_rows()
        '''除去表头需要遍历rows-1次'''
        for i in range(rows-1):
            '''给一个默认值'''
            cookies = None
            get_cookie = None
            headers = None
            '''i是从0开始，所以i+2，就和用例可以对应上，获取第i+2用例数据'''
            data = excel_data.get_rows_value(i+2)
            is_run = data[2]
            '''判断如果第二列数据为yes则执行'''
            if is_run == "yes":
                '''获取前置条件'''
                is_depend = data[3]
                '''如果前置条件存在，获取依赖字段'''
                data1 = json.loads(data[7])
                if is_depend:
                    depend_key = data[4]
                    depend_data  = get_data(is_depend)
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
                    get_cookie = {"is_cookie":"web"}
                    '''操作header的情况'''
                if header_method == "yes":
                    headers = getHeader.get_header()
                '''用封装的request发送请求'''
                res = request.run_main(method=method,url=url,get_cookie = get_cookie,cookies = cookies,headers = headers,data=data1)
                '''调试打印'''

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
                    config_msg = data_result.get_result(url,code)
                    '''进行断言'''
                    if msg == config_msg:
                        excel_data.excel_write_data(i + 2,13,"case通过")
                    else:
                        excel_data.excel_write_data(i + 2, 13, "case失败")
                        '''如果断言方法是result'''
                if assertion_method == "result":
                    '''这块需要注意返回结果获取的result是整型，而我们Excel中获取
                    的是字符串，所以这边需要把格式统一再做比对'''
                    if str(res["errorCode"]) == excepect_result:
                        excel_data.excel_write_data(i + 2, 13, "case通过")
                    else:
                        excel_data.excel_write_data(i + 2, 13, "case失败")

if __name__ == '__main__':
    run = RunMain()
    run.run_case()