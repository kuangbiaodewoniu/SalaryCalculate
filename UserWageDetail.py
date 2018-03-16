# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:Administrator
@file: UserWageDetail.py
@time: 2018/03/17
"""
import os,sys,csv

class UserWageDetail(object):

    def __init__(self, value):
        self.file_path = value

    def write_list_to_file(self,data):
        with open(self.file_path,'a',newline = "") as file:
            writer = csv.writer(file,dialect = "excel")
            writer.writerow(data)

if __name__ == '__main__':
    config_file = os.path.join(sys.path[0], 'userdata.csv')
    print (config_file)
    uwd = UserWageDetail(config_file)
    a = ['a','b','c']

    uwd.write_list_to_file(a)
    uwd.write_list_to_file(a)
    uwd.write_list_to_file(a)