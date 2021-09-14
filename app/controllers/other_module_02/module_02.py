# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 2:31 PM
# @Author  : yangyang
# @Email   : yangyang@ixiye.com
# @File    : cms_module_02.py
# @Software: PyCharm

from flask import Blueprint, render_template

route_module_02 = Blueprint('cms_module_02', __name__)


@route_module_02.route('/', methods=["GET", "POST"])
def module_02():
    return '其他业务模块002'


@route_module_02.route('/index', methods=["GET", "POST"])
def module_02_index():
    return render_template('index02.html')
