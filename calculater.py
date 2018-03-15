# !usr/bin/env python3
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: calculater.py 
@time: 2018/03/15 
"""

# 输出税后工资
# 计算过程需要扣除社会保险费用
# 支持多人同时计算工资
# 打印税后工资列表

import sys


def calc_real_wages(wages):
    # 应交保险 养老保险：8 %; 医疗保险：2 %; 失业保险：0.5 %; 工伤保险：0 %; 生育保险：0 %; 公积金：6 %
    insurance = wages * (0.08 + 0.02 + 0.005 + 0.06)

    # 起征点
    threshold = 3500

    # 应纳税所得额 = 工资金额 － 各项社会保险费 - 起征点(3500元)
    pay_taxes_amount = wages - insurance - threshold

    # 全月应纳税额	税率	速算扣除数（元）
    # 不超过 1500 元	3%	0
    # 超过 1500 元至 4500 元	10%	105
    # 超过 4500 元至 9000 元	20%	555
    # 超过 9000 元至 35000 元	25%	1005
    # 超过 35000 元至 55000 元	30%	2755
    # 超过 55000 元至 80000 元	35%	5505
    # 超过 80000 元	45%	13505
    taxes_rate = 0.03
    quick_calculation_deduction = 0

    if pay_taxes_amount <= 1500:
        taxes_rate = 0.03
        quick_calculation_deduction = 0
    elif pay_taxes_amount <= 4500:
        taxes_rate = 0.1
        quick_calculation_deduction = 105
    elif pay_taxes_amount <= 9000:
        taxes_rate = 0.2
        quick_calculation_deduction = 555
    elif pay_taxes_amount <= 35000:
        taxes_rate = 0.25
        quick_calculation_deduction = 1005
    elif pay_taxes_amount <= 55000:
        taxes_rate = 0.3
        quick_calculation_deduction = 2755
    elif pay_taxes_amount < 80000:
        taxes_rate = 0.35
        quick_calculation_deduction = 5505
    else:
        taxes_rate = 0.45
        quick_calculation_deduction = 13505

    # 应纳税额 = 应纳税所得额 × 税率 － 速算扣除数
    taxes_amount = pay_taxes_amount * taxes_rate - quick_calculation_deduction

    # 3500一下特殊处理
    if wages <= 3500:
        taxes_amount = 0

    # 实际工资
    real_wages = wages - insurance - taxes_amount

    # 特殊处理
    if real_wages < 0:
        real_wages = 0

    return  real_wages


if __name__ == '__main__':
    args = sys.argv[1:]
    wage_collection = {}
    for arg in args:
        arg_list =  arg.split(':')
        try:
            wage = int(arg_list[1])
        except:
            print('Parameter Error')
            exit(0)
        result = calc_real_wages(wage)
        wage_collection[arg_list[0]] = format(result, '.2f')

    for key, val in wage_collection.items():
        print(key + ':'+ val)