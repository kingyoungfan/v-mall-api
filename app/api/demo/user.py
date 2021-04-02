from flask import jsonify
from flask_restful import Resource


class User(Resource):

    @staticmethod
    def get():
        return jsonify({
            'code': 0
        })
