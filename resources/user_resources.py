from flask import request, Response
from flask_restful import Resource

from controllers.post_user import post_user  # , get_user
from models.user_model import UserModel
from schemas.user_schema import UserSchema

user_schema = UserSchema()


class User(Resource):
    def post(self):
        json_data = request.get_json()
        try:
            data = user_schema.load(json_data)
        except:
            return Response('Bad request', 400)
        response = post_user(data)
        return response

    # def get(self):
    #     response = get_user()
    #     return response
