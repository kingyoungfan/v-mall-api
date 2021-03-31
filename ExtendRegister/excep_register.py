# -*- coding: utf-8 -*-
# @Time    : 2021/3/19 12:18 PM
# @Author  : yangyang
# @Email   : yangyang@ixiye.com
# @File    : excep_register.py
# @Software: PyCharm

import os
import traceback

from flask import request, current_app
from werkzeug.exceptions import HTTPException

from app.api import route_api
from common.libs.customException import CustomException
from common.libs.api_result import api_result


@route_api.app_errorhandler(Exception)
def errors(e):
    traceback.print_exc()
    # current_app.logger.info('异常类型:', str(type(e)))

    if isinstance(e, CustomException):
        current_app.logger.info('-----CustomException-----')
        # tb('-----CustomException-----')
        return api_result(code=e.code, message='CustomException:【{}】'.format(str(e.msg)),
                          data=request.method + ' ' + request.path)

    if isinstance(e, HTTPException) and (300 <= e.code < 600):
        current_app.logger.info('-----HTTPException-----')
        current_app.logger.info('===>path is not found: ' + request.path)
        # tb('-----HTTPException-----')
        return api_result(code=e.code, message='HTTPException:【{}】'.format(str(e)),
                          data=request.method + ' ' + request.path)

    else:
        current_app.logger.info('-----Exception-----')
        # tb('-----Exception-----')
        return api_result(code=500, message='Exception:【{}】'.format(str(e)), data=request.method + ' ' + request.path)


if __name__ == '__main__':
    logs_path = os.getcwd() + '/logs/tb.log'
    print(logs_path)
