from flask import Response
from flask_restful import Resource

from controllers.info import get_info


class Info(Resource):
    def get(self):
        response = get_info()
        return response
