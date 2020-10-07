from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from controllers.post_fav import post_fav
from helpers.build_response import build_response
from schemas.favs_schema import FavsSchema

favourite_schema = FavsSchema()


class PostFavourite(Resource):
    @jwt_required
    def post(self, user_id):
        if get_jwt_identity() == user_id:
            json_data = request.get_json()
            try:
                data = favourite_schema.load(json_data)
            except:
                response = build_response(
                    {'error message': 'Bad request'}, 400)
                return response
            response = post_fav(data, user_id)
            return response
        else:
            response = build_response(
                {'error message': 'Invalid credentials'}, 403)
            return response
