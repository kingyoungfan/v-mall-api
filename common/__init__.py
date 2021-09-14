# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 10:37 AM

import base64
import hashlib
import hmac
import json
import time
from hashlib import md5

from Crypto.Cipher import AES


def token(message, enc=False, expire=3600 * 24):
    """
    token加密解密算法
    :param message:
    :param enc:
    :param expire:
    :return:
    """
    # 这个盐不能改😯
    salt = '0beb009a3213370e6cc54a7ebb989bf2e4db247fa115f31c6f95a94b7a0e'
    bs = 16
    pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
    unpad = lambda s: s[:-ord(s[len(s) - 1:])]
    if not enc:
        content, _time, _hmac = message[:-74], message[-74:-64], message[-64:]
        key = md5((_time + salt).encode("utf-8")).hexdigest()
        _i_hmac = hmac.new(bytes.fromhex(key), (content + _time).encode('utf-8'), hashlib.sha256).hexdigest()
        if _i_hmac != _hmac:
            return False
        if time.time() - int(_time) > expire:
            return False
        return json.loads(unpad(AES.new(key[:16], AES.MODE_CBC, key[16:]).decrypt(base64.b64decode(content))))
    else:
        # _time = str(time.time() - 1.3)[:10]
        _time = '1620110661'
        key = md5((_time + salt).encode("utf-8")).hexdigest()
        raw = pad(json.dumps(message))
        cipher = AES.new(key[:16], AES.MODE_CBC, key[16:])
        __time = _time.encode('utf-8')
        ret = base64.b64encode(cipher.encrypt(raw)) + __time
        ret_hmac = hmac.new(bytes.fromhex(key), ret, hashlib.sha256).hexdigest()

        return str(ret, encoding='utf-8') + ret_hmac


def token_uid(message):
    """
    获取uid
    :param message: uid加密信息
    :return: 用户主键
    """
    return int(token(message))


def pad(s):
    bs = 16
    return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)


if __name__ == '__main__':
    e_key = '87b105c8602290172260dd8e39d918bb'
    # print(token(123456, True))
    print(token('38hfKLpF9QqDSydIn41B9Q==162011066125b6a30ed40da6ea85ca7184052681de15631ae4ba3ef12ec804ea91245c1391'))
