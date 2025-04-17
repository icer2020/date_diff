#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-
#--------------------------------------------------
# Copyright (C) 2022 WayOn. All rights reserved.
# Filename      : date_diff.py
# Description   :  
# Date          : 2024-02-02
# Author        : Li Guoqiang
# Email         : lgq@way-on.com
# Version       : v0.10
# History       : initial version
#--------------------------------------------------

import datetime

start_default = '2024/10/06'
end_default = datetime.datetime.now().strftime("%Y/%m/%d")

start = input("请输入起始日期, 格式YYYY/MM/DD, 直接回车使用默认日期：2024/10/06: ")
end = input(f'请输入截至日期, 格式YYYY/MM/DD, 直接回车使用当天：{end_default}: ')

if start =="":
    start = start_default
if end =="":
    end = end_default

s_y = int(start.split('/')[0].lstrip('0'))
s_m = int(start.split('/')[1].lstrip('0'))
s_d = int(start.split('/')[2].lstrip('0'))

e_y = int(end.split('/')[0].lstrip('0'))
e_m = int(end.split('/')[1].lstrip('0'))
e_d = int(end.split('/')[2].lstrip('0'))

s = datetime.date(s_y, s_m, s_d)
e = datetime.date(e_y, e_m, e_d)

# 计算两个日期之间的差异
delta = e - s

# 获取天数差
days = delta.days
print(f'The days gap between {start} and {end} gap is: {days} day(s)') # 输出结果为31天
