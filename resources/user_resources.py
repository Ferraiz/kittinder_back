from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from helpers.build_response import build_response
from controllers.get_user import get_user
from controllers.login_user import login_user
from controllers.post_user import post_user
from controllers.put_user import put_user
from models.user_model import UserModel
from schemas.user_schema import UserSchema

user_schema = UserSchema()


class CreateUser(Resource):
    def post(self):
        json_data = request.get_json()
        try:
            data = user_schema.load(json_data)
        except:
            return build_response({'error message': 'Bad request'}, 400)
        response = post_user(data)
        return response


class UpdateUser(Resource):
    @jwt_required
    def put(self, user_id):
        if get_jwt_identity() == user_id:
            json_data = request.get_json()
            try:
                data = user_schema.load(json_data)
            except:
                return build_response({'error message': 'Bad request'}, 400)
            response = put_user(data, user_id)
            return response
        else:
            response = build_response(
                {'error message': 'Invalid credentials'}, 403)
            return response


class GetUser(Resource):
    @jwt_required
    def get(self, user_email):
        if get_jwt_identity() == user_id:
            response = get_user(user_email)
            return response
        else:
            response = build_response(
                {'error message': 'Invalid credentials'}, 403)
            return response


class UserLogin(Resource):
    def post(self):
        json_data = request.get_json()
        try:
            data = user_schema.load(json_data)
        except:
            return build_response({'error message': 'Bad request'}, 400)
        response = login_user(data)
        return response
