# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 3:15 PM
# @Author  : yangyang
# @Email   : yangyang@ixiye.com
# @File    : ApiHook.py
# @Software: PyCharm

from flask import request

from app.controllers.cms.cms_bp import route_admin


@route_admin.before_request
def before_request_cms():
    print('cms before_request')
    path = request.path
    print(path)

    if '/cms' in path:
        print('访问cms')
        return
