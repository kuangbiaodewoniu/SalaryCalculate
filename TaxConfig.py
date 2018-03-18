# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:Administrator
@file: TaxConfig.py
@time: 2018/03/16
配置文件格式示例：
JiShuL = 2193.00
JiShuH = 16446.00
YangLao = 0.08
YiLiao = 0.02
ShiYe = 0.005
GongShang = 0
ShengYu = 0
GongJiJin = 0.06
"""
import sys,os

class Config(object):

    def __init__(self,value):
        self.file_path = value

    def get_config_item(self, key):
        try:
            with open(self.file_path, 'r', encoding='UTF-8') as file:
                for str_line in file:
                    list_line = str_line.split('=')
                    if list_line[0].strip() == key:
                        return  float(list_line[1].strip())
            return 0
        except FileNotFoundError:
            print ('FileNotFoundError')
            exit(-1)


if __name__ == '__main__':
    config_file = os.path.join(sys.path[0], 'config.cfg')
    print (config_file)
    instance = Config(config_file)
    result = instance.get_config_item('ShiYe')
    print (result)

