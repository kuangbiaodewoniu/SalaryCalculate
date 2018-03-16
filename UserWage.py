# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:Administrator
@file: UserWage.py
@time: 2018/03/16
"""
import os,sys,csv

class UserWage(object):

    def __init__(self, value):
        self.file_path = value

    def get_all_wages(self):
        result = {}
        with open(self.file_path, 'r') as file:
            file_content = csv.reader(file)
            for line in file_content:
                result[line[0]] = float(line[-1])
        return result


if __name__ == '__main__':
    config_file = os.path.join(sys.path[0], 'UserWage.csv')
    # print (config_file)
    wage = UserWage(config_file)
    result = wage.get_all_wages()
    print (result)
