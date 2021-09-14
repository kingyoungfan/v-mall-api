from ExtendRegister.db_register import db
from app.models.base import Model
from common.libs.BaseModel import BaseModel

"""
 定义实体类
"""


class User(Model):
    # 定义表名
    __tablename__ = 'user'
    mobile = db.Column(db.String(11), unique=True)
    name = db.Column(db.String(64))
    sex = db.Column(db.Integer)
    age = db.Column(db.Integer)

    def __repr__(self):
        return '<user {}>'.format(self.name)
