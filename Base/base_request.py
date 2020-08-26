# -*-coding:utf-8-*-
import requests
from Base.handle_init import *
from Base.handle_cookie import *


class Method:

    def post(self,url,data,get_coookie,**kwargs):
        response = requests.post(url,data,**kwargs)

        if get_coookie != None:
            cookie_value = response.cookies

            cookie_value = requests.utils.dict_from_cookiejar(cookie_value)

            handlecookie.updata_cookie_value(cookie_value,get_coookie["is_cookie"])

        res = response.text
        return res
    def get(self,url,get_cookie,**kwargs):
        response = requests.get(url=url,**kwargs)
        if get_cookie != None:
            cookie_value = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value)
            handlecookie.updata_cookie_value(cookie_value,get_cookie["is_cookie"])
        res = response.text
        return res

    def run_main(self,method,url,data=None,get_cookie = None,**kwargs):
        '''通过传入的参数来判断调用上面的post还是get方法'''
        host = handle_ini.get_value()
        bas_url = host+"/"+url
        '''此句如果加上就返回mock文档里的数据，如果注释掉运行run_main就正常运行'''
        # return getValue.getvalue(url)

        if method =="get":
            res = self.get(bas_url,get_cookie,**kwargs)
        else:

            res = self.post(bas_url,data,get_cookie,**kwargs)
        '''此处代码是对返回的response进行反序列化处理，方便后续通过字典的key值来取对应的value近而进行断言'''
        try:
            res = json.loads(res)
        except:
            print("解析失败")
        return res

request = Method()

