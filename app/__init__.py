# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 10:11 AM
# @Author  : yangyang
# @Email   : yangyang@ixiye.com
# @File    : __init__.py.py
# @Software: PyCharm
from run import app


@app.route('/')
def index():
    return 'success'
