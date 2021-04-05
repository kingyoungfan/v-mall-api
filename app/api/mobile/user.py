# -*- coding: utf-8 -*-
# @author: yangyang
# @date 4/2/21 16:51
from flask import Blueprint, request, current_app

from ExtendRegister.redis_register import R
from app.api.mobile import mobile_bp


@mobile_bp.route('/index')
def index():
    """
    手机端首页
    :return: 首页数据
    """
    token = request.headers.get("token")
    current_app.logger.info('===>token: ' + token)

    p = R.pipeline()
    r_key = 'R_TOKEN_15857162155'
    p.set(r_key, token)
    p.execute()

    r_val = str(R.get(r_key))
    current_app.logger.info('===>r_val: ' + r_val)

    return {'code': 0, 'msg': 'mobile index', 'r_val': r_val}
