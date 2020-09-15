from flask import request, Response
from flask_restful import Resource

from controllers.post_user import post_user
from models.user_model import UserModel
from schemas.user_schema import UserSchema

user_schema = UserSchema()


class User(Resource):
    def post(self, email):
        response = post_user(email)
        return response
