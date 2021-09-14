# -*- coding: utf-8 -*-
# @Time    : 2021/3/19 10:31 AM
# @Author  : yangyang
# @Email   : yangyang@ixiye.com
# @File    : m1.py
# @Software: PyCharm

from flask import request


def rule_test02():
    if request.method == 'GET':
        print('get')
    if request.method == 'POST':
        print('post')
    return 'cms_module_02'
