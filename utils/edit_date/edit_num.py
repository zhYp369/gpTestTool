#!/usr/bin/env python3
# coding=utf-8

import time
import random


# 根据格式获取当前时间 （"%Y-%m-%dT%H:%M:%S"）
def get_time(template):
    now_time = time.strftime(template, time.localtime())
    return now_time


# 获取随机数
def get_random(num):
    suiji = ""
    for i in range(num):
        suiji = suiji + str(random.randint(0, 9))
    return suiji



