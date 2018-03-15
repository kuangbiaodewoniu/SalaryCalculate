# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: calculater.py 
@time: 2018/03/15 
"""

import sys

# 工资
try:
    wages = int(sys.argv[1])
except ValueError:
    print('Parameter Error')
    exit(0)

# 应交保险
insurance = 0
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

# 特殊处理
if taxes_amount < 0:
    taxes_amount = 0

# 格式化两位
format_taxes_amount = format(taxes_amount, '.2f')

print(format_taxes_amount)









