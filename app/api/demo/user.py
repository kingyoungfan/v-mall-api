from flask import jsonify
from flask_restful import Resource

from ExtendRegister.db_register import db
from app.models.user.user import User


class UserApi(Resource):

    @staticmethod
    def get():

        user = User(mobile='15857162166', name='xx')
        db.session.add(user)
        db.session.commit()
        return jsonify({
            'code': 0
        })
