# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 3:15 PM
# @Author  : yangyang
# @Email   : yangyang@ixiye.com
# @File    : ApiHook.py
# @Software: PyCharm

from flask import request

from ApplicationExample import create_app

app = create_app()


@app.before_request
def before_request_api():
    """
    PC端app拦截器
    :return:
    """
    print('app app app app')
    path = request.path
    print(path)
    return
