from ExtendRegister.db_register import db
from app.models.base import Model
from common.libs.BaseModel import BaseModel

"""
 定义实体类
"""


class User(Model):
    # 定义表名
    __tablename__ = 'user'
    mch_id = db.Column(db.Integer)
    mobile = db.Column(db.String(11), unique=True)
    name = db.Column(db.String(64))
    sex = db.Column(db.Integer)
    age = db.Column(db.Integer)
    nick_name = db.Column(db.String(64))
    avatar = db.Column(db.String(1024))
    open_id = db.Column(db.String(1024))

    def __repr__(self):
        return '<user {}>'.format(self.name)
