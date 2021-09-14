# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 3:15 PM
# @Author  : yangyang
# @Email   : yangyang@ixiye.com
# @File    : ApiHook.py
# @Software: PyCharm

from flask import request

from app.api import route_api


@route_api.before_request
def before_request_api():
    print('api before_request')
    path = request.path
    print(path)
    if request.method == 'OPTIONS':
        return
    if '/api' in path:
        print('访问api')
        return
