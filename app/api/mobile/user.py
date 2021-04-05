# -*- coding: utf-8 -*-
# @author: yangyang
# @date 4/2/21 16:51
from flask import Blueprint

mobile_bp = Blueprint('mobile', __name__)


@mobile_bp.route('/index')
def index():
    return {'code': 0, 'msg': 'mobile index'}
