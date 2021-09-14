# -*- coding: utf-8 -*-
# @author: yangyang
# @date 4/2/21 16:51


"""
管理后台接口
"""
from flask import Blueprint

user_bp = Blueprint('user', __name__)


@user_bp.route('/login')
def login():
    """
    管理后台用户登录
    :return:
    """
    return {"msg": "login success"}
