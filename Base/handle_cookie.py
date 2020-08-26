# -*-coding:utf-8-*-
from Base.handle_value import *
now_dir = os.path.dirname(os.path.dirname(__file__))
print(now_dir)
cookie_dir = now_dir +"/Config/cookie.json"

class HandleCookie:
    '''写入cookie'''
    def write_cookie(self, data, file_name="cookie.json"):
        data_value = json.dumps(data)
        with open(now_dir + "/Config/" + file_name,"w") as f:
            f.write(data_value)
    '''获取cookie'''
    def get_cookie_value(self,cookie_key):
        data = getValue.readjson("cookie.json")
        return data[cookie_key]

    '''根据key值更新cookie'''
    def updata_cookie_value(self, data, cookie_key):
        data1 = getValue.readjson("cookie.json")
        data1[cookie_key] = data
        self.write_cookie(data1)

handlecookie = HandleCookie()
