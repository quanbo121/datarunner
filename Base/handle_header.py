# -*-coding:utf-8-*-
from Base.handle_value import *

class HundleHeader:
    def get_header(self):
        return getValue.readjson("header.json")

getHeader = HundleHeader()
