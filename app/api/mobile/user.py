# -*- coding: utf-8 -*-
# @author: yangyang
# @date 4/2/21 16:51
from flask import Blueprint, request, current_app

from app.api.mobile import mobile_bp


@mobile_bp.route('/index')
def index():
    token = request.headers.get("token")
    current_app.logger.info('===>token: ' + token)

    return {'code': 0, 'msg': 'mobile index'}
