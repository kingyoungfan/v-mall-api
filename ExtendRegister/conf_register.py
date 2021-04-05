# -*- coding: utf-8 -*-
# @Time    : 2021/3/19 11:45 AM
# @Author  : yangyang
# @Email   : yangyang@ixiye.com
# @File    : conf_register.py
# @Software: PyCharm

from config.config import config_obj


def register_config(app):
    """配置文件"""

    """
    暂时兼容旧注册配置文件,后续废除。
    """
    # 旧注册配置文件
    # app.config.from_object(config_obj[app_conf()])  # 环境配置
    # config_obj[app_conf()].init_app(app)

    # 新注册配置文件
    app.config.from_object(config_obj['config'])  # 环境配置

    app.logger.info(config_obj['config'])
    # config_obj['config'].init_app(app)
