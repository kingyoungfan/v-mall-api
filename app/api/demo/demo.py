# -*- coding: utf-8 -*-
# @Time    : 2021-03-20 17:05
# @Author  : yangyang
# @Email   : yangyang@ixiye.com
# @File    : demo.py
# @Software: PyCharm

import requests

from flask_restful import Resource

from common.libs.customException import ab_code, ab_code_2


class Index(Resource):

    def get(self):
        import os
        import threading
        from flask import jsonify
        print("===>111")
        return jsonify({
            'path:"/api/"': 'flask api',
            'threading': threading.get_ident(),
            '当前进程id': os.getpid(),
            '父进程id': os.getppid(),
        })


class DemoApi(Resource):
    """
    参数使用:
        url不传参数则使用默认参数 page=1, size=10
    """

    def get(self, page=1, size=10):
        return 'flask resful get 参数{},{}'.format(page, size)

    def post(self, page=1, size=10):
        return 'flask resful post 参数{},{}'.format(page, size)

    def put(self, page=1, size=10):
        return 'flask resful put 参数{},{}'.format(page, size)

    def delete(self, page=1, size=10):
        return 'flask resful delete 参数{},{}'.format(page, size)


class HttpExceptionTest(Resource):

    def get(self):
        """
        测试HTTP异常

        :return:
        """
        # 模拟一个没有的url发出请求
        r = requests.get('http://0.0.0.0:9999/api/xxxx')
        return r.json()


class CustomExceptionTest(Resource):

    def get(self):
        """
        测试自定义异常

        :return:
        """
        # MethodView 自定义异常
        # ab_code(333)

        # flask_restful 自定义异常
        ab_code_2(333)


class BaseExceptionTest(Resource):

    def get(self):
        """
        测试内部异常

        :return:
        """
        1 / 0
        return
