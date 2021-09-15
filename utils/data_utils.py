#coding:utf-8
import time

dt = "2021-09-25 22:28:54"

#转换为时间数组
timeArray = time.strptime(dt, "%Y-%m-%d %H%M%S")
#转换为时间戳
timestamp = time.mktime(timeArray)