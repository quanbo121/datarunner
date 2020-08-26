# -*-coding:utf-8-*-
import configparser
import os
class HandleInit:

    def load_ini(self):
        '''获取工程目录'''
        main_path = os.path.dirname(os.path.dirname(__file__))
        '''拼接出ini文件的目录'''
        configfile_path = main_path + "/Config/server.ini"
        '''实例化对象'''
        cf = configparser.ConfigParser()
        cf.read(configfile_path,encoding="utf-8-sig")
        return cf
    '''获取ini文件的值'''
    def get_value(self,section="server",option="host"):
        cf = self.load_ini()
        try:
            data = cf.get(section,option)
        except:
            print("未获取到值")
            data =None
        return data
handle_ini = HandleInit()

