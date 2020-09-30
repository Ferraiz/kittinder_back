from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from controllers.get_kitties import get_kitties
from controllers.get_kitty import get_kitty
from controllers.post_kitty import post_kitty
from controllers.get_kitty_by_id import get_kitty_by_id
from controllers.put_kitty import put_kitty
from controllers.delete_kitty import delete_kitty
from helpers.build_response import build_response
from schemas.kitty_schema import KittySchema

kitty_schema = KittySchema()


class PostKitty(Resource):
    @jwt_required
    def post(self, user_id):
        json_data = request.get_json()
        try:
            data = kitty_schema.load(json_data)
        except:
            response = build_response({'error message': 'Bad request'}, 400)
            return response
        print(data)
        response = post_kitty(data, user_id)
        return response


class GetKitties(Resource):
    @jwt_required
    def get(self, user_id):
        response = get_kitties(user_id)
        return response


class GetKittyById(Resource):
    @jwt_required
    def get(self, user_id, kitty_id):
        response = get_kitty_by_id(user_id, kitty_id)
        return response


class GetKitty(Resource):
    @jwt_required
    def get(self):
        response = get_kitty()
        return response


class UpdateKitty(Resource):
    @jwt_required
    def put(self, user_id, kitty_id):
        json_data = request.get_json()
        try:
            data = kitty_schema.load(json_data)
        except:
            return build_response({'error message': 'Bad request'}, 400)
        response = put_kitty(data, user_id, kitty_id)
        return response


class DeleteKitty(Resource):
    @jwt_required
    def delete(self, user_id, kitty_id):
        print(user_id)
        print(kitty_id)
        response = delete_kitty(user_id, kitty_id)
        return response
