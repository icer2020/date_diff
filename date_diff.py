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

# start_default = '2024/10/08'
start_default = end_default = datetime.datetime.now().strftime("%Y/%m/%d")
end_default = end_default = datetime.datetime.now().strftime("%Y/%m/%d")

start = input(f'Please enter start date, format: YYYY/MM/DD(default is today {start_default}): ')
end = input(f'Please enter end date, format: YYYY/MM/DD(default is today: {end_default}): ')

start = start_default if start=="" else start
end = end_default if end=="" else end

delta = datetime.datetime.strptime(end,"%Y/%m/%d") -  datetime.datetime.strptime(start,"%Y/%m/%d")

# 获取天数差
days = delta.days
print(f'The days gap between {start} and {end} gap is: {days} day(s). Equal {int(days/7)} week(s) and {days%7} day(s)') # 输出结果为31天
