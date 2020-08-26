# -*-coding:utf-8-*-
'''导入实例化后的对象getValue，获取json文件内容'''
from Base.handle_value import getValue
class HandleResult:
    def get_result(self,url,Code):
        data = getValue.getvalue(url,"code_message.json")
        '''遍历获取后的列表'''
        for i in data:
            '''通过传入的code获取对应的值'''
            messaga = i.get(str(Code))
            '''如果message不为空，则返回'''
            if messaga:
                return messaga
            '''如果获取不到message值情况返回空'''
        return None
data_result = HandleResult()
