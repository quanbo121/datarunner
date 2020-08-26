# -*-coding:utf-8-*-
from Base.handle_excel import *
from jsonpath_rw import *
import json
'''拆分前置条件'''
def split_data(data):
    case_id = data.split(">")[0]
    rule_data = data.split(">")[1]
    return case_id,rule_data
'''根据前置条件获取依赖数据'''
def depend_data(data):
    case_id =split_data(data)[0]
    '''获取行号'''
    row_number = excel_data.get_rows_number(case_id)
    '''此处获取某单元格的函数之前hand_excle中已经封装好这里直接用'''
    data = excel_data.get_cell_value(row_number,14)

    return data

'''根据匹配规则和响应数据来获取依赖字段'''
def get_depend_data(res_data,key):
    res_data = json.loads(res_data)
    '''加载规则key'''
    json_exe = parse(key)
    '''根据规则再数据res_data寻找'''
    madle = json_exe.find(res_data)

    '''返回依赖字段返回的是列表，所以加【0】返回成字符串'''
    return [math.value for math in madle][0]


'''根据前置条件获取，获取依赖字段'''
def get_data(data):
    res_data  = depend_data(data)
    rule_data = split_data(data)[1]
    return get_depend_data(res_data,rule_data)
if __name__ == '__main__':
    data = "imooc_001>status"
    key = "status"
    print(get_data(data))