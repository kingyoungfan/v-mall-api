# -*- coding: utf-8 -*-
# @Time    : 2021-03-17 11:29
# @Author  : yangyang
# @Email   : yangyang@ixiye.com
# @File    : tools.py
# @Software: PyCharm


def check_keys(dic, *keys):
    for k in keys:
        if k not in dic.keys():
            return False
    return True
