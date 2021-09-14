# -*- coding: utf-8 -*-
# @Time    : 2021/3/19 12:00 PM
# @Author  : yangyang
# @Email   : yangyang@ixiye.com
# @File    : api_result.py
# @Software: PyCharm


from flask import jsonify


# 返回格式
def api_result(code=None, message=None, data=None, details=None, status=None):
    result = {
        "code": code,
        "message": message,
        "data": data,
    }

    if not result['data']:
        result.pop('data')
        return jsonify(result)
    return jsonify(result)


