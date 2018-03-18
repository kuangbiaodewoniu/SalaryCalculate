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

import sys,os
from user import UserWage
from TaxConfig import Config

def calc_real_wages(job_num,wages,JShuL,JShuH,YangLao,YiLiao,ShiYe,GongShang,ShengYu,GongJiJin):
    # JiShuL 为社保缴费基数的下限，即工资低于 JiShuL 的值的时候，需要按照 JiShuL 的数值乘以缴费比例来缴纳社保。
    # JiShuH 为社保缴费基数的上限，即工资高于 JiShuH 的值的时候，需要按照 JiShuH 的数值乘以缴费比例缴纳社保。
    ji_shu = wages
    if wages < JShuL:
        ji_shu = JShuL

    if wages > JShuH:
        ji_shu = JShuH

    # 应交保险 养老保险：8 %; 医疗保险：2 %; 失业保险：0.5 %; 工伤保险：0 %; 生育保险：0 %; 公积金：6 %

    insurance = ji_shu * (YangLao + YiLiao + ShiYe + GongShang + ShengYu+ GongJiJin)

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
    # 工号, 税前工资, 社保金额, 个税金额, 税后工资
    # print ([job_num, wages, format(insurance,'.2f'), format(taxes_amount,'.2f'), format(real_wages,'.2f')])
    return [job_num, int(wages), format(insurance,'.2f'), format(taxes_amount,'.2f'), format(real_wages,'.2f')]


if __name__ == '__main__':
    # 取参数文件

    args = sys.argv[1:]
    param_c_index = args.index('-c')
    tax_config_path = args[param_c_index+1]

    param_d_index = args.index('-d')
    usr_info_config_path = args[param_d_index+1]

    param_o_index = args.index('-o')
    wages_detail_config_path = args[param_o_index + 1]

    # 获取用户信息
    # user_info_file_path = os.path.join(sys.path[0], 'UserWage.csv')
    user = UserWage(usr_info_config_path)
    wage_info = user.get_user_wage()

    # 获取个税配置
    # config_file_path = os.path.join(sys.path[0], 'config.cfg')
    config = Config(tax_config_path)
    JShuL = config.get_config_item('JiShuL')
    JShuH = config.get_config_item('JiShuH')
    YangLao = config.get_config_item('YangLao')
    YiLiao = config.get_config_item('YiLiao')
    ShiYe = config.get_config_item('ShiYe')
    GongShang = config.get_config_item('GongShang')
    ShengYu = config.get_config_item('ShengYu')
    GongJiJin = config.get_config_item('GongJiJin')

    for user_num, wage in wage_info.items():
        # 计算工资
        wage_detail = calc_real_wages(user_num, wage, JShuL, JShuH, YangLao, YiLiao, ShiYe, GongShang, ShengYu, GongJiJin)

        # 保存信息
        # save_wage_path = os.path.join(sys.path[0], 'userdata.csv')
        save_wage = UserWage(wages_detail_config_path)
        save_wage.write_list_to_file(wage_detail)