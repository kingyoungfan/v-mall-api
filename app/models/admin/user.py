from ExtendRegister.db_register import db
from common.libs.BaseModel import BaseModel

"""
 定义实体类
"""


class User(BaseModel):
    # 定义表名
    __tablename__ = 'user'
    id = db.Column(db.BIGINT, primary_key=True)
    mobile = db.Column(db.String(11), unique=True)
    name = db.Column(db.String(64))
    sex = db.Column(db.Integer)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    update_at = db.Column(db.DATETIME)

    def __repr__(self):
        return '<user {}>'.format(self.name)
