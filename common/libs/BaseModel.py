# -*- coding: utf-8 -*-
# @Time    : 2021-03-16 17:06
# @Author  : yangyang
# @Email   : yangyang@ixiye.com
# @File    : BaseModel.py
# @Software: PyCharm

import json
from datetime import datetime

from ExtendRegister.db_register import db


class BaseModel(db.Model):
    """
    id: 主键
    create_at:创建时间
    update_at:最后更新更新
    """
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='id')
    create_at = db.Column('create_time', db.DateTime, default=datetime.now, comment='创建时间(结构化时间)')
    update_at = db.Column('update_time', db.DateTime, default=datetime.now, onupdate=datetime.now,
                          comment='更新时间(结构化时间)')

    def add(self, commit=False):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def keys(self):
        """
        返回所有字段对象
        :return:
        """
        return self.__table__.columns

    def __getitem__(self, item):
        return getattr(self, item)

    def to_json(self):

        """
        旧方法
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
            del dict["_update_timestamp"]
            del dict["_create_timestamp"]
            del dict["_create_time"]
            del dict["_update_time"]
            del dict["_status"]
            if str(self.__table__) == 'cms_user':
                del dict["_password"]
        """

        d = {}
        dict = self.__dict__
        [d.update({i.name: dict.get(i.name, '')}) for i in self.keys()]
        # print(d)

        d['create_time'] = str(d.get('create_time')) if d.get('create_time') else None
        d['update_time'] = str(d.get('update_time')) if d.get('update_time') else None

        # del d["update_timestamp"]
        # del d["create_timestamp"]
        # del d["create_time"]
        # del d["update_time"]
        # del d["status"]

        return d

    def update(self, **kwargs):
        # print('self->', self)
        for attr, value in kwargs.items():
            # print(self, attr, type(attr), value, type(value))
            try:  # 部分属性无法setattr
                setattr(self, attr, json.dumps(value, ensure_ascii=False) if isinstance(value, dict) else str(value))
            except BaseException as e:
                print('update error {}'.format(str(e)))
        return self

    def delete_obj(self):
        self.status = 2
        db.session.commit()
