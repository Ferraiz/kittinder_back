from flask import request, Response
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from controllers.login_user import login_user
from controllers.post_user import post_user  # , get_user
from controllers.put_user import put_user
from models.user_model import UserModel
from schemas.user_schema import UserSchema

user_schema = UserSchema()


class CreateUser(Resource):
    def post(self):
        json_data = request.get_json()
        print(json_data)
        try:
            data = user_schema.load(json_data)
        except:
            return Response('Bad request', 400)
        response = post_user(data)
        return response


class ChangeUser(Resource):
    @jwt_required
    def put(self, user_id):
        json_data = request.get_json()
        print(json_data)
        try:
            data = user_schema.load(json_data)
        except:
            return Response('Bad request', 400)
        response = put_user(data, user_id)
        return response


class UserLogin(Resource):
    def post(self):
        json_data = request.get_json()
        try:
            data = user_schema.load(json_data)
        except:
            return Response('Bad request', 400)
        response = login_user(data)
        return response
