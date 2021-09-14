# -*- coding: utf-8 -*-
# @author: yangyang
# @date 4/14/21 15:32
from flask import request

from app.api.mobile import mobile_bp


@mobile_bp.before_request
def mobile_before_request_api():
    """
    移动端拦截器
    :return:
    """
    print('===>mobile api before_request')
    token = request.headers.get("token")
    if token is None:
        pass
    path = request.path
    print(path)
    if request.method == 'OPTIONS':
        return
    if '/api' in path:
        print('访问api')
        return
