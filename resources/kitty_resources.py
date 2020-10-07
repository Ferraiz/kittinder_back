from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
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
        if get_jwt_identity() == user_id:
            json_data = request.get_json()
            try:
                data = kitty_schema.load(json_data)
            except:
                response = build_response(
                    {'error message': 'Bad request'}, 400)
                return response
            response = post_kitty(data, user_id)
            return response
        else:
            response = build_response(
                {'error message': 'Invalid credentials'}, 403)
            return response


class GetKitties(Resource):
    @jwt_required
    def get(self, user_id):
        if get_jwt_identity() == user_id:
            limit = request.args.get('limit', type=int)
            page = request.args.get('page', type=int)
            response = get_kitties(user_id, limit, page)
            return response
        else:
            response = build_response(
                {'error message': 'Invalid credentials'}, 403)
            return response


class GetKittyById(Resource):
    @jwt_required
    def get(self, user_id, kitty_id):
        if get_jwt_identity() == user_id:
            response = get_kitty_by_id(user_id, kitty_id)
            return response
        else:
            response = build_response(
                {'error message': 'Invalid credentials'}, 403)
            return response


class GetKitty(Resource):
    @jwt_required
    def get(self):
        response = get_kitty()
        return response


class UpdateKitty(Resource):
    @jwt_required
    def put(self, user_id, kitty_id):
        if get_jwt_identity() == user_id:
            json_data = request.get_json()
            try:
                data = kitty_schema.load(json_data)
            except:
                return build_response({'error message': 'Bad request'}, 400)
            response = put_kitty(data, user_id, kitty_id)
            return response
        else:
            response = build_response(
                {'error message': 'Invalid credentials'}, 403)
            return response


class DeleteKitty(Resource):
    @jwt_required
    def delete(self, user_id, kitty_id):
        response = delete_kitty(user_id, kitty_id)
        return response
