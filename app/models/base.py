# -*- coding: utf-8 -*-
# @author: yangyang
# @date 4/2/21 17:04
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base

from ExtendRegister.db_register import db

Base = declarative_base()

session = db.session


class Model(db.Model):
    """Mixin that adds convenience methods for CRUD (create, read, update, delete) operations."""

    @classmethod
    def create(cls, **kwargs):
        """Create a new record and save it the database."""
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=False, **kwargs):
        """Update specific fields of a record."""
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=False):
        """Save the record."""
        session.add(self)
        if commit:
            session.commit()
        return self

    def delete(self, commit=False):
        """Remove the record from the database."""
        session.delete(self)
        return commit and session.commit()

    @classmethod
    def get_by(cls, **kwargs):
        return session.query(cls).filter_by(**kwargs)

    @classmethod
    def get_by_uid(cls, record_uid):
        """Get record by ID."""
        if any(
                (isinstance(record_uid, str) and record_uid.isdigit(),
                 isinstance(record_uid, (int, float))),
        ):
            return cls.get_by(uid=record_uid).first()
        return None

    @classmethod
    def get_by_id(cls, _id):
        if any(
                (isinstance(_id, str) and _id.isdigit(),
                 isinstance(_id, (int, float))),
        ):
            return cls.get_by(id=_id).first()

        return None

    """Base model class that includes CRUD convenience methods."""

    __abstract__ = True
    """
        id: 主键
        create_at:创建时间
        update_at:最后更新更新
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='id')
    created_at = db.Column('created_at', db.DateTime, default=datetime.now, comment='创建时间(结构化时间)')
    update_at = db.Column('update_at', db.DateTime, default=datetime.now, onupdate=datetime.now,
                          comment='更新时间(结构化时间)')

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    def __getitem__(self, item):
        return getattr(self, item)

    def keys(self):
        """
        返回所有字段对象
        :return:
        """
        return self.__table__.columns
