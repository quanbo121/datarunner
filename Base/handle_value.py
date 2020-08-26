# -*-coding:utf-8-*-
import json
import os
'''获取当前目录，并拼接出json文件的路径--json_dir'''
now_dir = os.path.dirname(os.path.dirname(__file__))
mock_dir = now_dir +"/Config/mock_response_data.json"
class GetValue:
    def readjson(self,file_name = None):
        '''默认file_name参数为None，可以进行mock需要的数据的获取'''
        if file_name == None:
            json_dir = mock_dir
            '''否则就按照填入的参数来获取json文件'''
        else:
            json_dir = now_dir+"/Config/"+file_name
            '''因为code_message数据里可能含有中文，这里要加上编码encoding的参数utf-8'''
        with open(json_dir,encoding="UTF-8") as f:
            data = json.load(f)
        return data

    def getvalue(self,key,file_name = None):
        data = self.readjson(file_name)
        # return data[key]
        return data.get(key)



getValue = GetValue()

