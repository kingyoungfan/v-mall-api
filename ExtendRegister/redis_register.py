# -*- coding: utf-8 -*-
# @author: yangyang
# @date 4/5/21 16:20
from flask_redis import FlaskRedis

R = FlaskRedis()


def get_str(r_key):
    """
    从redis中获取str值
    :param r_key: redis key
    :return: val
    """
    return R.get(r_key).decode('utf-8')


def set_val(r_key, val):
    """
    写入redis缓存
    :param r_key:
    :param val:
    :return:
    """
    p = R.pipeline()
    p.set(r_key, val)
    p.execute()


def set_val_at(r_key, val, expire_at):
    """
    写入redis缓存
    :param r_key:
    :param val:
    :param expire_at: 在改时刻过期
    :return:
    """
    p = R.pipeline()
    p.set(r_key, val)
    p.expireat(r_key, expire_at)
    p.execute()
